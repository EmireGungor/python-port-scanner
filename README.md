# Network Port Scanner & Service Banner Grabber

A lightweight Python tool for TCP port scanning and basic service banner identification. Built for learning, security lab environments, and simple network diagnostics.

> ⚠️ Only scan hosts you own or have explicit permission to test.

---

## 🚀 Features

- **V1.0 - TCP Connect Scanner:** Determines port state with a full TCP connect scan using `socket.connect_ex()`. The operating system performs the TCP handshake; a return value of `0` means the port is open.
- **V2.0 - Banner Grabbing:** For every open port, reads the first line the service returns (passive banner read). On port `8080`, the scanner first sends an HTTP `HEAD` request so the web server replies with its status line.
- **V3.0 - CLI Argument Parsing:** `argparse`-based command-line interface. Target host and port range are configured at runtime instead of being hardcoded.
- **Planned:** Multi-threaded scanning (`concurrent.futures.ThreadPoolExecutor`) for faster scans over wide port ranges.

---

## 🛠️ Requirements & Environment

- **OS:** Linux (tested on Ubuntu 26.04 LTS / VirtualBox)
- **Language:** Python 3.x
- **Dependencies:** Built-in `socket` and `argparse` modules only (no third-party packages)

---

## 💻 Usage

### 1. (Optional) Start a Test HTTP Service

To simulate an open port locally, start a temporary web server on port `8080`:

```bash
python3 -m http.server 8080
```

### 2. Run the Scanner

```bash
python3 port_scanner.py -t <target_ip> -p <start-end>
```

**Arguments:**

| Flag | Long form  | Required | Default  | Description                            |
|------|------------|----------|----------|----------------------------------------|
| `-t` | `--target` | Yes      | —        | Target IPv4 address to scan            |
| `-p` | `--ports`  | No       | `1-1024` | Port range in `start-end` format       |

**Example:**

```bash
python3 port_scanner.py -t 127.0.0.1 -p 8075-8085
```

---

## 📊 Sample Output

```text
--- V2.0 Banner Scan: 127.0.0.1 ---
[-] Port 8078: KAPALI
[-] Port 8079: KAPALI
[+] Port 8080: ACIK  --> Banner: HTTP/1.0 200 OK
[-] Port 8081: KAPALI
```

---

## ⚙️ How It Works

1. `parse_ports()` converts the `start-end` string into a list of port numbers.
2. For each port, a TCP socket is created with a 2-second timeout.
3. `connect_ex()` attempts a connection. `0` → port reported as **ACIK** (open); any other result → **KAPALI** (closed).
4. On an open port, the scanner tries to read up to 1024 bytes and prints the first line as the banner. If nothing is received within the timeout, it prints `Banner Alinamadi`.

---

## 🚧 Known Limitations

- Ports are scanned sequentially, so large ranges are slow (multi-threading is planned).
- The port argument must be a range; a single port must be written as `80-80`.
- Filtered ports (no response / timeout) are reported as **KAPALI** and are not distinguished from closed ports.
- The HTTP probe is only sent on port `8080`, and its `Host` header is fixed to `127.0.0.1`.

---

## 📁 Project Structure

```text
python-port-scanner/
├── port_scanner.py   # Argument parsing, scanning and banner grabbing
└── README.md         # Project documentation
```

---

## 👤 Author

GitHub: [@EmireGungor](https://github.com/EmireGungor)


