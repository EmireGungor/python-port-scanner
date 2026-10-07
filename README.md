# Network Port Scanner & Service Banner Grabber

A lightweight, modular Python-based network reconnaissance tool built to perform TCP port scanning and service banner identification. Designed for security analysis, penetration testing labs, and network diagnostics.

---

## 🚀 Features

- **V1.0 - Core TCP Scanner:** Checks active TCP port states (OPEN/CLOSED) via IPv4 socket connections using 3-way handshake checks (`socket.connect_ex`).
- **V2.0 - Banner Grabbing:** Sends an HTTP probe to open ports to retrieve service banners and header signatures (currently targets port 8080; general banner grabbing is planned).
- **V3.0 - CLI Argument Parsing:** Added `argparse`-based command-line interface. Target host and port range are now configurable at runtime instead of hardcoded.
- **Planned:** Multi-threaded scanning (`concurrent.futures.ThreadPoolExecutor`) for high-speed performance across wide port ranges.

---

## 🛠️ Requirements & Environment

- **OS:** Linux (Tested on Ubuntu 26.04 LTS / VirtualBox)
- **Language:** Python 3.x
- **Dependencies:** Built-in `socket` and `argparse` modules only (no external third-party installations required)

---

## 💻 Usage

### 1. (Optional) Spin up a Test HTTP Service

To simulate an active open port locally, start a temporary web server on port `8080`:

```bash
python3 -m http.server 8080
```

### 2. Run the Port Scanner

```bash
python3 port_scanner.py -t <target_ip> -p <port_range>
```

**Arguments:**

| Flag | Long form    | Required | Default   | Description                          |
|------|--------------|----------|-----------|---------------------------------------|
| `-t` | `--target`   | Yes      | —         | Target IPv4 address to scan           |
| `-p` | `--ports`    | No       | `1-1024`  | Port range to scan, `start-end` format |

**Example:**

```bash
python3 port_scanner.py -t 127.0.0.1 -p 1-8100
```

---

## 📊 Sample Output


```bash
--- V2.0 Banner Scan: 127.0.0.1 ---
[-] Port 21 : KAPALI
[-] Port 22 : KAPALI
[-] Port 80 : KAPALI
[-] Port 443 : KAPALI
[+] Port 8080 : ACIK --> Banner: HTTP/1.0 200 OK
```

---

## 📁 Project Structure

```bash
python-port-scanner/
├── port_scanner.py # Main scanner script: argument parsing, scanning, banner grabbing
└── README.md # Project documentation
```

---

## 👤 Author
```bash
GitHub: [@EmireGungor](https://github.com/EmireGungor)
```
