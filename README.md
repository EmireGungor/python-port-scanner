# Python Port Scanner & Banner Grabber

A small Python networking project built to practice **TCP socket programming, port-state checks, timeouts, and basic banner grabbing** using only the Python standard library. The current version performs a sequential TCP connect scan against a predefined list of ports and attempts to read the first line returned by services on open ports.

> ⚠️ **Disclaimer:** This project is intended for learning, lab environments, and networks you are authorized to test.

---

## Current Version — V2.0

### Features
- TCP port checks using `socket.AF_INET` and `socket.SOCK_STREAM`
- Open/closed detection with `connect_ex()`
- Configurable socket timeout
- Basic banner retrieval with `recv()`
- HTTP `HEAD` request for the local test service on port `8080`
- No third-party dependencies

---

## Default Scan Configuration

```python
target_ip = "127.0.0.1"
ports = [21, 22, 80, 443, 8080]
```

The project intentionally keeps the target and port list simple so the focus stays on understanding the underlying socket workflow before adding CLI parsing and concurrency.

---

## How It Works

For each configured TCP port, the script:
1. Creates a TCP socket.
2. Applies a 2-second timeout.
3. Attempts a connection with `connect_ex()`.
4. Marks the port as open when the connection succeeds.
5. Attempts to read up to 1024 bytes from the service.
6. Prints the first returned line as a basic banner.
7. Closes the socket before moving to the next port.

*Note: For port 8080, the scanner sends an HTTP HEAD request first so it can retrieve a response from a local Python HTTP server.*

---

## Requirements

- Python 3.x
- Linux, macOS, or Windows with Python socket support
- No external Python packages required

---

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/EmireGungor/python-port-scanner.git
cd python-port-scanner
```

### 2. Optional: Start a local HTTP test service
```bash
python3 -m http.server 8080
```

### 3. Run the scanner
```bash
python3 port_scanner.py
```

---

## Example Output

```text
--- V2.0 Banner Scan: 127.0.0.1 ---
[-] Port 21: KAPALI
[-] Port 22: KAPALI
[-] Port 80: KAPALI
[-] Port 443: KAPALI
[+] Port 8080: ACIK --> Banner: HTTP/1.0 200 OK
```

---

## Version Progress

### V1.0 — Basic TCP Scanner
- Initial TCP socket implementation
- Basic open/closed port checks
- Sequential scanning

### V2.0 — Banner Grabbing (Current)
- Added service-response reading with `recv()`
- Added HTTP request handling for the local port 8080 test case
- Added simple banner output

### V3.0 — Planned
- Command-line arguments with `argparse`
- User-defined target and port ranges
- Concurrent scanning for improved performance
- Stronger input validation and error handling
- Cleaner result formatting

---

## Current Limitations

- Target IP and port list are hard-coded.
- Scanning is sequential.
- TCP only; UDP is not supported.
- Banner grabbing depends on the service returning data.
- The HTTP request is currently specific to the local port 8080 test case.

---

## What I Practiced

- Python socket programming
- TCP connection behavior
- Timeouts and connection-result handling
- Basic service banner collection
- Incremental development from a simple scanner toward a more usable CLI tool

---

## Author

**Emire Güngör**  
Software Engineering Student — OSTİM Technical University  
GitHub: [@EmireGungor](https://github.com/EmireGungor)
