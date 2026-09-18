<div align="center">

# 🔴 REVERSE SHELL v2

### TCP • COMMANDS • FILES • SCREENSHOTS

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=700&color=FF0000&center=true&vCenter=true&width=650&lines=AUTHORIZED+LAB+MODE;TCP+CHANNEL+ONLINE;COMMAND+MODULE+ONLINE;FILE+TRANSFER+ONLINE;SCREENSHOT+MODULE+ONLINE" alt="Animated status">

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,50:660000,100:ff0000&height=120&section=header&text=REVERSE%20SHELL%20V2&fontSize=28&fontColor=ffffff&animation=twinkling" width="100%">

<a href="https://github.com/romilleuva/reverse-shell-v2">
<img src="https://img.shields.io/github/stars/romilleuva/reverse-shell-v2?style=for-the-badge&color=ff0000&labelColor=080808">
</a>
<a href="https://github.com/romilleuva/reverse-shell-v2">
<img src="https://img.shields.io/github/languages/top/romilleuva/reverse-shell-v2?style=for-the-badge&color=990000&labelColor=080808">
</a>

<br><br>

<img src="https://skillicons.dev/icons?i=python,linux,git,github&theme=dark">

</div>

---

## ⚡ Overview

A Python client/server project for learning:

- TCP socket communication
- JSON messaging
- Command execution
- Screenshot transfer
- File upload and download

> 🔴 Use only on systems you own or are explicitly authorized to test.

---

## 🧬 Architecture

```mermaid
flowchart LR
    A["🔴 Control Node<br/>Exploit.py"]
    B["⚡ TCP :9999"]
    C["💻 Client<br/>Client.py"]

    A <-->|Commands / JSON| B
    B <-->|Requests / Responses| C

    C --> D["📸 Screenshot"]
    C --> E["📁 File Transfer"]
    C --> F["⌨️ Command Output"]

    style A fill:#080808,stroke:#ff0000,color:#fff
    style B fill:#220000,stroke:#ff3333,color:#fff
    style C fill:#080808,stroke:#cc0000,color:#fff
```

---

## 🔴 Modules

| Module | Status |
|---|---|
| TCP communication | 🔴 Online |
| Remote commands | 🔴 Online |
| Screenshot capture | 🔴 Online |
| File upload/download | 🔴 Online |
| JSON protocol | 🔴 Online |
| Interactive CLI | 🔴 Online |

---

## 🚀 Quick Start

```bash
git clone [https://github.com/romilleuva/reverse-shell-v2.git](https://github.com/romilleuva/reverse-shell-v2.git)
cd reverse-shell-v2
pip install pyautogui
```

### Control node

```bash
python Exploit.py
```

### Authorized lab client

```bash
python Client.py
```

Default connection:

```text
127.0.0.1:9999
```

---

## 🖥️ Demo Flow

```mermaid
sequenceDiagram
    participant C as Control Node
    participant S as TCP Socket
    participant V as Lab Client

    C->>S: Send command
    S->>V: Forward request
    V->>V: Execute authorized action
    V-->>S: JSON / binary response
    S-->>C: Display result
```

---

## 🛡️ Safety

✅ Personal machines  
✅ Isolated virtual labs  
✅ CTF environments  
✅ Authorized penetration tests  

❌ Unauthorized systems  
❌ Credential theft  
❌ Data theft  
❌ Production systems without permission  

---

## 🧰 Project Structure

```text
reverse-shell-v2/
├── Client.py
├── Exploit.py
├── README.md
└── assets/
```

---

## 🗺️ Roadmap

```mermaid
graph LR
    A["Current Build"] --> B["Protocol Cleanup"]
    B --> C["Testing"]
    C --> D["Safer Lab Controls"]
    D --> E["Better CLI"]

    style A fill:#ff0000,color:#fff
    style B fill:#330000,color:#fff
    style C fill:#330000,color:#fff
    style D fill:#330000,color:#fff
    style E fill:#330000,color:#fff
```

---

<div align="center">

### 👤 ROMIL LEUVA

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=900&color=FF0000&center=true&vCenter=true&width=550&lines=PYTHON+ENTHUSIAST;CYBERSECURITY+LEARNER;BUILD+%E2%86%92+BREAK+%E2%86%92+LEARN" alt="Author animation">

<br>

⭐ Star the repository if it helped you learn.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,50:660000,100:ff0000&height=100&section=footer&text=HACK%20ETHICALLY&fontSize=24&fontColor=ffffff&animation=twinkling" width="100%">

</div>
