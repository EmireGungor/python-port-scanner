"""Black-box tests: run port_scanner.py as a subprocess against sockets on 127.0.0.1.

Only localhost is ever scanned. Run from the repo root:
    py -3 -m unittest discover -s tests -v
"""
import socket
import subprocess
import sys
import threading
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "port_scanner.py"
HOST = "127.0.0.1"


def run_scanner(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), "-t", HOST, *args],
        capture_output=True, text=True, timeout=30,
    )


def free_port():
    """Bind to port 0, let the OS pick a free port, then release it (now closed)."""
    with socket.socket() as s:
        s.bind((HOST, 0))
        return s.getsockname()[1]


class FakeService:
    """A one-shot TCP server that optionally sends a banner after accepting."""

    def __init__(self, banner=None):
        self.banner = banner
        self.sock = socket.socket()
        self.sock.bind((HOST, 0))
        self.sock.listen(1)
        self.port = self.sock.getsockname()[1]
        self.thread = threading.Thread(target=self._serve, daemon=True)

    def _serve(self):
        try:
            conn, _ = self.sock.accept()
        except OSError:
            return
        with conn:
            if self.banner:
                conn.sendall(self.banner)
            conn.settimeout(3)
            try:
                conn.recv(1024)  # keep the connection open until the scanner closes it
            except OSError:
                pass

    def __enter__(self):
        self.thread.start()
        return self

    def __exit__(self, *exc):
        self.sock.close()
        self.thread.join(timeout=5)


class ScannerTests(unittest.TestCase):
    def test_closed_port_reported_kapali(self):
        port = free_port()
        result = run_scanner("-p", f"{port}-{port}")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"[-] Port {port}: KAPALI", result.stdout)

    def test_open_port_with_banner(self):
        with FakeService(banner=b"SSH-2.0-TestServer\r\n") as svc:
            result = run_scanner("-p", f"{svc.port}-{svc.port}")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(f"[+] Port {svc.port}: ACIK", result.stdout)
        self.assertIn("SSH-2.0-TestServer", result.stdout)

    def test_open_port_without_banner(self):
        # The scanner waits for its 2 s timeout, then falls back to the message.
        with FakeService(banner=None) as svc:
            result = run_scanner("-p", f"{svc.port}-{svc.port}")
        self.assertIn(f"[+] Port {svc.port}: ACIK", result.stdout)
        self.assertIn("Banner Alinamadi", result.stdout)

    @unittest.expectedFailure
    def test_single_port_without_range(self):
        # Known limitation (README): "-p 80" crashes with IndexError; it must be "80-80".
        # Remove @expectedFailure once parse_ports accepts a single port.
        port = free_port()
        result = run_scanner("-p", str(port))
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
