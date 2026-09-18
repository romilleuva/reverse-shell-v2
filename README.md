<div align="center"> <!-- HERO --> <img src="./assets/banner.svg" alt="Reverse Shell v2" width="100%"/> <br> <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&duration=2500&pause=700&color=FF1A1A&center=true&vCenter=true&width=750&lines=REMOTE+ACCESS+%2F%2F+CONTROL+%2F%2F+TRANSFER;PYTHON+%2B+TCP+%2B+SOCKETS;RED+TEAM+LAB+TOOLKIT;BUILT+FOR+ETHICAL+HACKING+%26+EDUCATION" alt="Typing animation"/>
<br><br>

<br> <a href="https://github.com/romilleuva/reverse-shell-v2"> <img src="https://img.shields.io/github/stars/romilleuva/reverse-shell-v2?style=flat-square&color=ff0000&label=STARS"/> </a> <a href="https://github.com/romilleuva/reverse-shell-v2"> <img src="https://img.shields.io/github/forks/romilleuva/reverse-shell-v2?style=flat-square&color=990000&label=FORKS"/> </a> <a href="https://github.com/romilleuva/reverse-shell-v2"> <img src="https://img.shields.io/github/last-commit/romilleuva/reverse-shell-v2?style=flat-square&color=cc0000&label=LAST%20COMMIT"/> </a>

<br><br>

⚠️ EDUCATIONAL SECURITY TOOL

This project is intended for authorized security research, controlled lab environments,
CTFs, and cybersecurity education. Only use it on systems you own or have explicit
permission to test.

</div> 🩸 > WHOAMI
Reverse Shell v2 is a Python-based client/server security-learning project demonstrating how a TCP socket connection can be used to establish an interactive remote command channel.

The project currently demonstrates:

🖥️ Remote command execution

📸 Live screenshot capture

📤 File upload

📥 File download

🔌 TCP client/server communication

🐍 Python socket programming

🧵 Thread-based connection handling

🖥️ Interactive terminal interface

The goal is learning how remote-control channels work, not providing a production-ready remote administration system.

🔴 > SYSTEM STATUS
╔══════════════════════════════════════════════════════════════╗
║ REVERSE SHELL v2.0 ║
╠══════════════════════════════════════════════════════════════╣
║ STATUS : ONLINE ║
║ PROTOCOL : TCP ║
║ LANGUAGE : PYTHON ║
║ ARCHITECTURE : CLIENT / SERVER ║
║ MODE : EDUCATIONAL SECURITY RESEARCH ║
║ UI : INTERACTIVE TERMINAL ║
╚══════════════════════════════════════════════════════════════╝

⚡ > CAPABILITIES

<div align="center"> Module Capability Status 01 Remote command execution 🔴 ACTIVE 02 Screenshot capture 🔴 ACTIVE 03 File upload 🔴 ACTIVE 04 File download 🔴 ACTIVE 05 TCP communication 🔴 ACTIVE 06 Interactive command interface 🔴 ACTIVE </div> 🧬 > ARCHITECTURE flowchart LR
A["🖥️ CONTROL NODE<br/>Exploit.py"]
B["🔌 TCP SOCKET"]
C["💻 CLIENT<br/>Client.py"]

A -->|Connect / Commands| B
B -->|TCP Channel| C

C -->|Command Output| B
B -->|Response| A

A --> D["📸 Screenshot"]
A --> E["📤 Upload"]
A --> F["📥 Download"]

style A fill:#050505,stroke:#ff0000,color:#ff3333
style B fill:#0b0000,stroke:#990000,color:#ffffff
style C fill:#050505,stroke:#ff0000,color:#ff3333
style D fill:#120000,stroke:#cc0000,color:#ffffff
style E fill:#120000,stroke:#cc0000,color:#ffffff
style F fill:#120000,stroke:#cc0000,color:#ffffff

Data Flow
┌───────────────────────┐
│ CONTROL │
│ Exploit.py │
└───────────┬───────────┘
│
│ TCP
▼
╔═══════════════════════╗
║ SOCKET CHANNEL ║
╚═══════════╤═══════════╝
│
▼
┌───────────────────────┐
│ CLIENT │
│ Client.py │
└───────────┬───────────┘
│
┌────────────────┼────────────────┐
▼ ▼ ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ COMMAND │ │ SCREEN │ │ FILES │
│ EXEC │ │ CAPTURE │ │ TRANSFER │
└──────────┘ └──────────┘ └──────────┘

🕸️ > FEATURE MATRIX
🖥️ Remote Command Channel

The control side provides an interactive terminal-style interface for sending commands to the connected client and receiving command output.

[client-host]$ whoami

[+] command sent
[+] response received

📸 Screenshot Capture

The project includes a screenshot command that requests a screenshot from the client and transfers the resulting data back to the control side.

[client-host]$ screenshot

[+] requesting screenshot
[+] receiving image data
[+] displaying result

📤 File Upload

Files can be transferred from the control side to the connected client.

[client-host]$ upload <file>

📥 File Download

Files can also be transferred from the connected client back to the control side.

[client-host]$ download <file>

🧰 > TECH STACK

<div align="center"> <img src="https://skillicons.dev/icons?i=python,linux,git,github&theme=dark" alt="Tech stack"/> </div> LANGUAGE ───────► Python NETWORKING ───────► TCP / Sockets ARCHITECTURE ───────► Client / Server CONCURRENCY ───────► Python Threads DATA ───────► Socket Streams / JSON INTERFACE ───────► Interactive CLI
📁 > PROJECT STRUCTURE
reverse-shell-v2/
│
├── 🔴 Client.py
│ └── Client-side connection & command handling
│
├── 🔴 Exploit.py
│ └── Server/control-side implementation
│
├── 📝 README.md
│ └── Project documentation
│
└── 🎨 assets/
├── banner.svg
├── architecture.svg
└── terminal.gif

🚀 > QUICK START

Clone
git clone https://github.com/romilleuva/reverse-shell-v2.git
cd reverse-shell-v2

Start the control side
python Exploit.py

Start the client

Run Client.py only inside your authorized lab/test environment and configure the connection endpoint required by the project.

python Client.py

💡 For security testing, use an isolated VM/lab network rather than a third-party or production system.

🧪 > LAB WORKFLOW
┌────────────────────────────────────────────────────────────┐
│ CONTROLLED LAB │
├────────────────────────────────────────────────────────────┤
│ │
│ ┌──────────────┐ ┌──────────────┐ │
│ │ SECURITY │ │ TEST │ │
│ │ VM / HOST │ │ VM │ │
│ └──────┬───────┘ └──────┬───────┘ │
│ │ │ │
│ │ TCP LAB CHANNEL │ │
│ └──────────────────────────────────┘ │
│ │
│ 🧪 AUTHORIZED TEST ENVIRONMENT │
│ │
└────────────────────────────────────────────────────────────┘

🔥 > COMMAND CONCEPT

The interactive interface follows a simple command-channel model:

                USER INPUT
                    │
                    ▼
           ┌─────────────────┐
           │ COMMAND PARSER  │
           └────────┬────────┘
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
  COMMAND       SCREENSHOT       FILE
   MODE           MODE          MODE
      │             │             │
      ▼             ▼             ▼
   SEND TCP      IMAGE DATA    TRANSFER
      │             │             │
      └─────────────┼─────────────┘
                    ▼
                RESPONSE

🧠 > WHAT THIS PROJECT TEACHES

This project can be useful for studying:

Python socket programming

TCP client/server architecture

Network communication

Command-channel design

Threading and concurrent connections

Binary data transfer

File-transfer protocols

Security tooling concepts

Red-team lab fundamentals

Detection opportunities for remote-control channels

🛡️ > SECURITY & ETHICS

This repository demonstrates functionality that can be dual-use.

Use it responsibly.

╔══════════════════════════════════════════════════════════╗
║ AUTHORIZATION RULE ║
╠══════════════════════════════════════════════════════════╣
║ ║
║ ✔ Your own computer ║
║ ✔ Your own virtual machines ║
║ ✔ Authorized penetration-testing labs ║
║ ✔ CTF / educational environments ║
║ ✔ Systems where you have explicit permission ║
║ ║
║ ✘ Unauthorized computers ║
║ ✘ Third-party systems ║
║ ✘ Production systems without authorization ║
║ ✘ Credential/data theft ║
║ ║
╚══════════════════════════════════════════════════════════╝

The author is not responsible for misuse of this project.

📸 > VISUAL DEMO

Put your own screenshots/GIFs inside assets/ and replace the placeholders below:

<div align="center"> <img src="./assets/terminal.gif" width="90%" alt="Terminal demonstration"/>
<br><br>

<img src="./assets/architecture.svg" width="90%" alt="Architecture diagram"/> </div>
Recommended assets
assets/
├── banner.svg ← animated red/black hero
├── terminal.gif ← terminal demo
├── architecture.svg ← network diagram
├── screenshot.png ← screenshot feature
└── workflow.gif ← project workflow

📊 > PROJECT TELEMETRY

<div align="center"> <img src="https://github-readme-stats.vercel.app/api/pin/?username=romilleuva&repo=reverse-shell-v2&theme=dark&title_color=ff0000&icon_color=ff0000&text_color=ffffff&bg_color=050505&border_color=660000" alt="Repository statistics"/> </div> 🩸 > ROADMAP [✓] TCP client/server communication [✓] Remote command execution [✓] Screenshot capture [✓] File upload/download [ ] Cleaner command protocol [ ] Better connection handling [ ] Improved error handling [ ] Safer lab configuration [ ] Automated testing [ ] Documentation improvements [ ] Better UI / terminal experience
🤝 > CONTRIBUTING

Contributions are welcome when they improve the project's educational value, reliability, documentation, or safe lab usage.

FORK
│
▼
CREATE BRANCH
│
▼
MAKE CHANGES
│
▼
TEST IN LAB
│
▼
COMMIT
│
▼
PULL REQUEST

Please avoid contributions intended to facilitate unauthorized access, credential theft, persistence, evasion, or deployment against systems without permission.

🐛 > REPORTING ISSUES

When opening an issue, include:

Operating system

Python version

Error message

Relevant logs

Reproduction steps

Whether the issue occurs on the client or control side

Never include passwords, tokens, private keys, or sensitive system information.

👤 > AUTHOR // ROMILLEUVA

<div align="center"> ROMIL LEUVA
FULL-STACK DEVELOPER · CYBERSECURITY ENTHUSIAST · PYTHON

╔══════════════════════════════════════════╗
║ ║
║ BUILD → BREAK → LEARN → BUILD ║
║ ║
╚══════════════════════════════════════════╝

Cybersecurity • Reverse Engineering • Python • Web Development

<br> <img src="https://skillicons.dev/icons?i=python,javascript,react,nextjs,nodejs,flask,git,github&theme=dark" alt="Skills"/>

<br><br>

<a href="https://github.com/romilleuva"> <img src="https://img.shields.io/badge/GitHub-romilleuva-111111?style=for-the-badge&logo=github&logoColor=ffffff"/> </a> <a href="https://github.com/romilleuva/reverse-shell-v2"> <img src="https://img.shields.io/badge/PROJECT-Reverse%20Shell%20v2-8B0000?style=for-the-badge&logo=github&logoColor=ffffff"/> </a> </div>

<div align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,50:660000,100:ff0000&height=120&section=footer" width="100%"/> // CONNECTION CLOSED [ SYSTEM ] Thank you for visiting. [ SYSTEM ] Stay curious. [ SYSTEM ] Hack ethically.
⭐ Star the repository if you found the project useful for learning.
