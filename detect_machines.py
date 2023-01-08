import platform
import socket

def get_os():
    os_name = platform.system()
    if os_name == "Windows":
        return "Windows"
    elif os_name == "Linux":
        return "Linux"
    elif os_name == "Darwin":
        return "MacOS"
    else:
        return "Other"

def scan_network():
    machines = {}
    for i in range(1, 255):
        try:
            ip = "192.168.1." + str(i)
            hostname = socket.gethostbyaddr(ip)[0]
            os = get_os()
            machines[ip] = (hostname, os)
        except:
            pass
    return machines

if __name__ == "__main__":
    machines = scan_network()
    for ip, info in machines.items():
        hostname, os = info
        print(f"IP: {ip}\tHostname: {hostname}\tOS: {os}")
