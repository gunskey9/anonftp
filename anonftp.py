import ftplib
import socket
import os
import os
import subprocess
from tqdm import tqdm

# Clear the screen
os.system('clear')

# Use subprocess to run the figlet command and capture its output
output = subprocess.check_output(["figlet", "-f", "slant", "-l", "-w", "160", "EkoAnonFTP"])

# Print the output
print('\033[93m' + output.decode() + '\033[0m')

PORT = 21

def anon_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        ftp.quit()
        print(f"\033[32m[*] {hostname} allows anonymous login on port {PORT}\033[0m")
        return True
    except ftplib.all_errors:
        return False

def check_visible_files(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login('anonymous', 'anonymous')
        ftp.cwd('/')
        files = ftp.nlst()
        visible_files = [f for f in files if f not in ('.', '..')]
        ftp.quit()
        if visible_files:
            print(f"\033[32m[*] Visible files on {host}: {visible_files}\033[0m")
            return visible_files
        else:
            return None
    except ftplib.all_errors:
        return None

def port_scan(host):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, PORT))
        s.send(b'Hello\r\n')
        banner = s.recv(1024)
        if banner:
            print(f"[*] Port {PORT} is open on {host}")
            if anon_login(host):
                visible_files = check_visible_files(host)
                if visible_files:
                    return host, visible_files
                else:
                    return host, None
        s.close()
    except:
        pass
    return None, None

def main():
    while True:
        file_loc = input("Enter the file location containing IPs (q to quit): ")
        if file_loc == 'q':
            break
        if not os.path.isfile(file_loc):
            print("File not found. Please try again.")
            continue
        with open(file_loc, 'r') as f:
            targets = f.read().splitlines()
        anon_hosts = []
        visible_files_hosts = []
        with tqdm(total=len(targets)) as pbar:
            for target in targets:
                pbar.set_description(f"Scanning target: {target} ({socket.gethostbyname(target)})")
                host, visible_files = port_scan(target)
                if host:
                    anon_hosts.append(host)
                    if visible_files:
                        visible_files_hosts.append((host, visible_files))
                pbar.update(1)
        if anon_hosts:
            print("\n[*] IPs allowing anonymous login:")
            print("\n".join(anon_hosts))
        if visible_files_hosts:
            print("\n[*] IPs with visible files on FTP server:")
            for host, visible_files in visible_files_hosts:
                print(f"{host}: {visible_files}")
    print("\nGoodbye.")

if __name__ == '__main__':
    main()import ftplib
import socket
import os
import os
import subprocess
from tqdm import tqdm

# Clear the screen
os.system('clear')

# Use subprocess to run the figlet command and capture its output
output = subprocess.check_output(["figlet", "-f", "slant", "-l", "-w", "160", "EkoAnonFTP"])

# Print the output
print('\033[93m' + output.decode() + '\033[0m')

PORT = 21

def anon_login(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        ftp.quit()
        print(f"\033[32m[*] {hostname} allows anonymous login on port {PORT}\033[0m")
        return True
    except ftplib.all_errors:
        return False

def check_visible_files(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login('anonymous', 'anonymous')
        ftp.cwd('/')
        files = ftp.nlst()
        visible_files = [f for f in files if f not in ('.', '..')]
        ftp.quit()
        if visible_files:
            print(f"\033[32m[*] Visible files on {host}: {visible_files}\033[0m")
            return visible_files
        else:
            return None
    except ftplib.all_errors:
        return None

def port_scan(host):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, PORT))
        s.send(b'Hello\r\n')
        banner = s.recv(1024)
        if banner:
            print(f"[*] Port {PORT} is open on {host}")
            if anon_login(host):
                visible_files = check_visible_files(host)
                if visible_files:
                    return host, visible_files
                else:
                    return host, None
        s.close()
    except:
        pass
    return None, None

def main():
    while True:
        file_loc = input("Enter the file location containing IPs (q to quit): ")
        if file_loc == 'q':
            break
        if not os.path.isfile(file_loc):
            print("File not found. Please try again.")
            continue
        with open(file_loc, 'r') as f:
            targets = f.read().splitlines()
        anon_hosts = []
        visible_files_hosts = []
        with tqdm(total=len(targets)) as pbar:
            for target in targets:
                pbar.set_description(f"Scanning target: {target} ({socket.gethostbyname(target)})")
                host, visible_files = port_scan(target)
                if host:
                    anon_hosts.append(host)
                    if visible_files:
                        visible_files_hosts.append((host, visible_files))
                pbar.update(1)
        if anon_hosts:
            print("\n[*] IPs allowing anonymous login:")
            print("\n".join(anon_hosts))
        if visible_files_hosts:
            print("\n[*] IPs with visible files on FTP server:")
            for host, visible_files in visible_files_hosts:
                print(f"{host}: {visible_files}")
    print("\nGoodbye.")

if __name__ == '__main__':
    main()
