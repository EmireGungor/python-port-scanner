import socket

target_ip = "127.0.0.1"
ports = [21, 22, 80, 443, 8080]

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
