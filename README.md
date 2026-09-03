# Network Port Scanner & Service Banner Grabber

A lightweight, modular Python-based network reconnaissance tool built to perform TCP port scanning and service banner identification. Designed for security analysis, penetration testing labs, and network diagnostics.

---

## 🚀 Features

- **V1.0 - Core TCP Scanner:** Checks active TCP port states (OPEN/CLOSED) via IPv4 socket connections using 3-way handshake checks.
- **V2.0 - Banner Grabbing:** Interrogates open ports with HTTP/TCP payload requests to retrieve running service banners and header signatures.
- **V3.0 (Planned):** Multi-threaded scanning for high-speed performance and Command Line Interface (CLI) argument parsing.

---

## 🛠️ Requirements & Environment

- **OS:** Linux (Tested on Ubuntu 26.04 LTS / VirtualBox)
- **Language:** Python 3.x
- **Dependencies:** Built-in `socket` module (No external third-party installations required).

---

## 💻 Usage

### 1. (Optional) Spin up a Test HTTP Service
To simulate an active open port locally, start a temporary web server on port `8080`:

```bash
python3 -m http.server 8080
 
### 2. Run the Port Scanner
In a new terminal window, execute the scanner script:

python3 port_scanner.py


📊 Sample Output
--- V2.0 Banner Scan: 127.0.0.1 ---
[-] Port 21   : KAPALI
[-] Port 22   : KAPALI
[-] Port 80   : KAPALI
[-] Port 443  : KAPALI
[+] Port 8080 : ACIK  --> Banner: HTTP/1.0 200 OK

👤 Author
    GitHub: @EmireGungor
