# python-port-scanner

Learning project: TCP connect scanner + banner grabber. Standard library only (`socket`, `argparse`); do not add third-party packages.

## Commands (Windows)
- Run: `py -3 port_scanner.py -t 127.0.0.1 -p 8075-8085`
- Test service: `py -3 -m http.server 8080`
- Tests: `py -3 -m unittest discover -s tests -v` (black-box, localhost only)

## Working rules
- Plan first: for any change beyond a one-line fix, propose a short plan and wait for approval before editing.
- After every change, run the tests and show the result. Add or update a test for new behavior.
- Only scan 127.0.0.1 or hosts the user owns. Never point tests or examples at external hosts.
- This is a learning project: explain the networking/OS concept behind a change (TCP handshake, timeouts, threads), not just the code.
- Keep README "Known Limitations" and the version string in sync with the code.
