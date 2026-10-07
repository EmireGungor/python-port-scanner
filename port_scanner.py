import socket
import argparse

def parse_ports(port_str):
    parts = port_str.split("-")
    ports = []
    for i in range(int(parts[0]), int(parts[1])+1):
	    ports.append(i)
    return ports

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target",  required=True)
parser.add_argument("-p", "--ports",  default="1-1024")
args = parser.parse_args()
target_ip =args.target
ports = parse_ports(args.ports)

print(f"--- V2.0 Banner Scan: {target_ip} ---")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    if s.connect_ex((target_ip, port)) == 0:
        if port == 8080:
            s.send(b"HEAD / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n")
        try:
            banner = s.recv(1024).decode().split('\n')[0]
        except:
            banner = "Banner Alinamadi"
        print(f"[+] Port {port}: ACIK  --> Banner: {banner}")
    else:
        print(f"[-] Port {port}: KAPALI")
    s.close()
