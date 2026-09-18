<div align="center">

# 🔴 REVERSE SHELL v2

### `REMOTE CONTROL • TCP SOCKETS • FILE TRANSFER • SCREEN CAPTURE`

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&duration=1800&pause=500&color=FF0000&center=true&vCenter=true&width=800&lines=INITIALIZING+REVERSE+SHELL+V2...;ESTABLISHING+TCP+CHANNEL...;CLIENT+%3C%3D%3E+CONTROL+NODE;COMMAND+CHANNEL+ONLINE;FILE+TRANSFER+ONLINE;SCREENSHOT+MODULE+ONLINE;AUTHORIZED+LAB+MODE+%5BACTIVE%5D" alt="Animated terminal"/>

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:050505,50:330000,100:ff0000&height=3&section=header" width="100%">

<br>

<a href="https://github.com/romilleuva/reverse-shell-v2">
<img src="https://img.shields.io/github/stars/romilleuva/reverse-shell-v2?style=for-the-badge&color=ff0000&labelColor=080808&logo=github" alt="Stars">
</a>
<a href="https://github.com/romilleuva/reverse-shell-v2/network/members">
<img src="https://img.shields.io/github/forks/romilleuva/reverse-shell-v2?style=for-the-badge&color=990000&labelColor=080808&logo=github" alt="Forks">
</a>
<a href="https://github.com/romilleuva/reverse-shell-v2/commits/main">
<img src="https://img.shields.io/github/last-commit/romilleuva/reverse-shell-v2?style=for-the-badge&color=cc0000&labelColor=080808&logo=git" alt="Last Commit">
</a>
<a href="https://github.com/romilleuva/reverse-shell-v2">
<img src="https://img.shields.io/github/languages/top/romilleuva/reverse-shell-v2?style=for-the-badge&color=660000&labelColor=080808&logo=python" alt="Python">
</a>

<br><br>

<img src="https://skillicons.dev/icons?i=python,linux,git,github&theme=dark" alt="Technology Stack">

<br><br>

> 🔴 **EDUCATIONAL SECURITY PROJECT**
>
> Designed for authorized security research, CTFs, cybersecurity labs, and learning.
> **Only use this software on systems you own or have explicit permission to test.**

</div>

---

<div align="center">

## `╔══[ SYSTEM IDENTIFICATION ]══╗`

```text
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   ██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗███████╗ │
│   ██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝ │
│   ██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝█████╗  ███████╗ │
│   ██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══╝  ╚════██║ │
│   ██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████╗███████║ │
│   ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝ │
│                                                              │
│                    R E V E R S E   S H E L L                 │
│                         V E R S I O N   2                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
🩸 > ABOUT
Reverse Shell v2 is a Python client/server project built to demonstrate TCP socket communication, interactive command execution, screenshot transfer, and bidirectional file transfer in a controlled environment.

The repository contains two primary components:

┌─────────────────────┐
│     Exploit.py      │
│   CONTROL / SERVER  │
└──────────┬──────────┘
           │
           │ TCP
           │
           ▼
┌─────────────────────┐
│      Client.py      │
│       CLIENT        │
└─────────────────────┘

The control side listens for connections while the client establishes the TCP connection and handles supported requests.

🔴 > LIVE SYSTEM
<div align="center">
╔════════════════════════════════════════════════════════════╗
║                     REVERSE SHELL v2                       ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  PROTOCOL        :: TCP                                    ║
║  LANGUAGE        :: PYTHON                                 ║
║  ARCHITECTURE    :: CLIENT / SERVER                        ║
║  CONTROL PORT    :: 9999                                   ║
║  COMMAND CHANNEL :: ACTIVE                                 ║
║  FILE TRANSFER   :: ACTIVE                                 ║
║  SCREEN CAPTURE  :: ACTIVE                                 ║
║                                                            ║
║  STATUS          :: ● ONLINE                               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff0000,50:660000,100:050505&height=4&section=header" width="80%"> </div>
⚡ > FEATURES
<div align="center">
MODULE	FUNCTION	STATUS
🖥️	Remote command execution	🔴 ONLINE
📸	Screenshot capture	🔴 ONLINE
📤	File upload	🔴 ONLINE
📥	File download	🔴 ONLINE
🔌	TCP socket communication	🔴 ONLINE
🧵	Threaded server handling	🔴 ONLINE
🧾	JSON message protocol	🔴 ONLINE
🖥️	Interactive CLI	🔴 ONLINE

</div>
🧬 > ARCHITECTURE
flowchart LR

    A["🔴 CONTROL NODE<br/><b>Exploit.py</b>"]
    B["⚡ TCP SOCKET<br/>:9999"]
    C["💻 CLIENT<br/><b>Client.py</b>"]

    A -->|"COMMAND"| B
    B -->|"TCP CHANNEL"| C
    C -->|"JSON RESPONSE"| B
    B -->|"OUTPUT"| A

    A --> D["📸 SCREENSHOT"]
    A --> E["📤 UPLOAD"]
    A --> F["📥 DOWNLOAD"]

    style A fill:#050505,stroke:#ff0000,color:#ff3333,stroke-width:3px
    style B fill:#100000,stroke:#ff0000,color:#ffffff,stroke-width:3px
    style C fill:#050505,stroke:#cc0000,color:#ff3333,stroke-width:3px
    style D fill:#120000,stroke:#ff0000,color:#ffffff
    style E fill:#120000,stroke:#ff0000,color:#ffffff
    style F fill:#120000,stroke:#ff0000,color:#ffffff

🔥 Communication Flow
                         ┌──────────────────────┐
                         │     CONTROL NODE     │
                         │      Exploit.py      │
                         └──────────┬───────────┘
                                    │
                                    │ COMMAND
                                    ▼
                         ╔══════════════════════╗
                         ║     TCP CHANNEL      ║
                         ║       :9999          ║
                         ╚══════════╤═══════════╝
                                    │
                                    │ REQUEST
                                    ▼
                         ┌──────────────────────┐
                         │        CLIENT        │
                         │       Client.py      │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    │               │                │
                    ▼               ▼                ▼
             ┌────────────┐  ┌────────────┐  ┌────────────┐
             │  COMMAND   │  │ SCREENSHOT │  │    FILE    │
             │ EXECUTION  │  │   MODULE   │  │  TRANSFER  │
             └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
                   │               │                │
                   └───────────────┼────────────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │       RESPONSE       │
                         │    JSON / BINARY     │
                         └──────────────────────┘

🕸️ > COMMAND CHANNEL
The control interface accepts commands and sends them through the established TCP connection.

┌─────────────────────────────────────────────────────────┐
│                    INTERACTIVE CLI                      │
└─────────────────────────────────────────────────────────┘

[hostname]$ whoami

[+] COMMAND
    │
    ▼
[+] TCP SEND
    │
    ▼
[+] CLIENT EXECUTION
    │
    ▼
[+] JSON RESPONSE
    │
    ▼
[+] OUTPUT DISPLAYED

Example:

[workstation]$ whoami

{
    "type": "cmd_result",
    "command": "whoami",
    "output": "user",
    "cwd": "/home/user",
    "hostname": "workstation"
}

📸 > SCREENSHOT ENGINE
The client uses PyAutoGUI to capture the screen and transfers the PNG data through the established socket connection.

                 SCREENSHOT REQUEST
                         │
                         ▼
                ┌─────────────────┐
                │    CLIENT.PY    │
                └────────┬────────┘
                         │
                         ▼
                 ┌───────────────┐
                 │   PyAutoGUI   │
                 └───────┬───────┘
                         │
                         ▼
                    PNG BUFFER
                         │
                         ▼
                  JSON METADATA
                         │
                         ▼
                    TCP STREAM
                         │
                         ▼
                ┌─────────────────┐
                │   CONTROL NODE  │
                └─────────────────┘

📦 > FILE TRANSFER
Upload
CONTROL NODE
     │
     │ file metadata
     ▼
   CLIENT
     │
     │ ACK
     ▼
CONTROL NODE
     │
     │ binary file data
     ▼
   CLIENT
     │
     ▼
 SAVED FILE

Download
CONTROL NODE
     │
     │ download request
     ▼
   CLIENT
     │
     │ file metadata
     ▼
CONTROL NODE
     │
     │ ACK
     ▼
   CLIENT
     │
     │ binary data
     ▼
CONTROL NODE
     │
     ▼
 SAVED FILE

🧰 > TECHNOLOGY
<div align="center"> <img src="https://skillicons.dev/icons?i=python,linux,git,github&theme=dark" width="350"> </div>
╔══════════════════════════════════════════════════════════╗
║                     TECHNOLOGY                           ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  LANGUAGE       → Python                                 ║
║  NETWORK        → TCP / IPv4                             ║
║  SOCKET API     → Python socket                          ║
║  PROTOCOL       → JSON + binary payloads                 ║
║  SCREENSHOT     → PyAutoGUI                              ║
║  COMMANDS       → subprocess / shell                    ║
║  CONCURRENCY    → Python threading                       ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

📁 > PROJECT STRUCTURE
reverse-shell-v2/
│
├── 🔴 Client.py
│   └── Client connection & request handling
│
├── 🔴 Exploit.py
│   └── Control/server implementation
│
├── 📄 README.md
│   └── Documentation
│
└── 📂 assets/
    └── Optional visual assets

🚀 > QUICK START
01 — Clone
git clone https://github.com/romilleuva/reverse-shell-v2.git
cd reverse-shell-v2

02 — Install dependency
The client uses PyAutoGUI for screenshots:

pip install pyautogui

03 — Start the control node
python Exploit.py

The current implementation listens on:

0.0.0.0:9999

04 — Start the client
For an authorized local/lab environment:

python Client.py

The default client configuration connects to:

127.0.0.1:9999

🧪 > DEMO ENVIRONMENT
╔══════════════════════════════════════════════════════════════╗
║                    CONTROLLED LAB                           ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   ┌─────────────────┐          ┌─────────────────┐           ║
║   │                 │          │                 │           ║
║   │  CONTROL VM     │          │    TEST VM      │           ║
║   │                 │          │                 │           ║
║   │   Exploit.py    │◄────────►│    Client.py    │           ║
║   │                 │   TCP    │                 │           ║
║   └─────────────────┘          └─────────────────┘           ║
║                                                              ║
║                  🔴 AUTHORIZED LAB ONLY 🔴                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

🎯 > USE CASES
This project is useful for learning about:

Python networking

TCP sockets

Client/server architecture

JSON-based messaging

Binary data transfer

Screenshot transmission

File transfer protocols

Interactive command channels

Threading

Security research

Controlled penetration-testing labs

Detection and monitoring of remote-control traffic

📡 > PROTOCOL
The project uses structured JSON messages for several operations.

{
  "type": "cmd_result",
  "command": "example",
  "output": "command output",
  "cwd": "/current/path",
  "hostname": "machine"
}

Screenshot metadata follows the same general message-oriented approach:

{
  "type": "screenshot",
  "size": 123456
}

File-transfer messages contain metadata such as:

{
  "type": "upload",
  "name": "example.txt",
  "size": 1024
}

🩸 > TERMINAL SIMULATION
┌──(romil㉿lab)-[~/reverse-shell-v2]
└─$ python Exploit.py

[+] Server Listening on 0.0.0.0:9999
[+] Connection received
[+] Hostname: LAB-CLIENT

[LAB-CLIENT]$ whoami
user

[LAB-CLIENT]$ screenshot
[+] Screenshot saved

[LAB-CLIENT]$ download example.txt
[+] File downloaded

[LAB-CLIENT]$ upload test.txt
[+] File uploaded

📊 > REPOSITORY
<div align="center"> <a href="https://github.com/romilleuva/reverse-shell-v2"> <img src="https://github-readme-stats.vercel.app/api/pin/?username=romilleuva&repo=reverse-shell-v2&theme=dark&bg_color=050505&title_color=ff0000&text_color=ffffff&icon_color=ff0000&border_color=660000" width="500" alt="Repository Card"> </a>
<br><br>

<img src="https://github-readme-stats.vercel.app/api?username=romilleuva&show_icons=true&hide_border=true&bg_color=050505&title_color=ff0000&text_color=ffffff&icon_color=ff0000&include_all_commits=true" width="500" alt="GitHub Stats"> </div>
🛣️ > ROADMAP
                    REVERSE SHELL v2
                           │
                           ▼
                 ┌───────────────────┐
                 │   CURRENT BUILD   │
                 └─────────┬─────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      COMMAND           SCREENSHOT        FILES
       CHANNEL            MODULE         TRANSFER
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  NEXT ITERATION │
                  └────────┬────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
         Protocol       Testing       UI / CLI
         cleanup       framework     improvements

Planned improvements
[✓] TCP client/server communication
[✓] Remote command execution
[✓] Screenshot capture
[✓] File upload
[✓] File download
[✓] JSON message handling
[✓] Interactive CLI

[ ] Improved protocol framing
[ ] Better connection lifecycle
[ ] Better error handling
[ ] Automated tests
[ ] Cleaner CLI
[ ] Improved documentation
[ ] Safer lab configuration
[ ] Better logging

🛡️ > SECURITY & ETHICS
This project provides functionality that can be dual-use.

Use it only in environments where you have authorization.

╔══════════════════════════════════════════════════════════╗
║                    AUTHORIZATION                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   ✓ Your own machines                                   ║
║   ✓ Your own virtual machines                           ║
║   ✓ Isolated cybersecurity labs                        ║
║   ✓ CTF environments                                    ║
║   ✓ Authorized penetration testing                      ║
║   ✓ Educational research                                ║
║                                                          ║
║   ✗ Unauthorized systems                                ║
║   ✗ Third-party machines                                ║
║   ✗ Production systems without permission               ║
║   ✗ Credential or data theft                             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

🐛 > BUG REPORTING
When reporting an issue, include:

Operating system

Python version

Error message

Relevant logs

Steps to reproduce

Client/control-side information

Never include:

Passwords

API keys

Tokens

Private keys

Personal data

Sensitive system information

🤝 > CONTRIBUTING
             ┌──────────────┐
             │     FORK     │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ CREATE BRANCH│
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ MAKE CHANGES │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ TEST IN LAB  │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │    COMMIT    │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ PULL REQUEST │
             └──────────────┘

Contributions that improve reliability, documentation, testing, protocol design, or safe educational use are welcome.

👤 > AUTHOR
<div align="center"> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=1000&color=FF0000&center=true&vCenter=true&width=650&lines=ROMIL+LEUVA;FULL-STACK+DEVELOPER;PYTHON+ENTHUSIAST;CYBERSECURITY+LEARNER;BUILD+%E2%86%92+BREAK+%E2%86%92+LEARN+%E2%86%92+BUILD" alt="Author animation"/>
<br><br>

<a href="https://github.com/romilleuva"> <img src="https://img.shields.io/badge/GITHUB-romilleuva-050505?style=for-the-badge&logo=github&logoColor=white&labelColor=660000"> </a> <a href="https://github.com/romilleuva/reverse-shell-v2"> <img src="https://img.shields.io/badge/REPOSITORY-REVERSE%20SHELL%20V2-050505?style=for-the-badge&logo=github&logoColor=white&labelColor=990000"> </a>
<br><br>

<img src="https://skillicons.dev/icons?i=python,javascript,react,nextjs,nodejs,flask,git,github&theme=dark" alt="Skills"> </div>
<div align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,35:330000,70:990000,100:ff0000&height=160&section=footer&text=CONNECTION%20CLOSED&fontSize=25&fontColor=ffffff&animation=twinkling&fontAlignY=65" width="100%"> <br>
[ SYSTEM ] CONNECTION CLOSED
[ SYSTEM ] STAY CURIOUS
[ SYSTEM ] KEEP LEARNING
[ SYSTEM ] HACK ETHICALLY

<br>
⭐ If this project helped you learn something, consider starring the repository.

</div> ```
