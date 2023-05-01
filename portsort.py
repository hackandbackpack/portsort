import os
import readline

def ip_sort_key(ip):
    return tuple(map(int, ip.split('.')))

# Reads the input file and returns a dictionary of port numbers and corresponding IP addresses
def read_file(file_path):
    ip_port_dict = {}
    with open(file_path, 'r') as f:
        for line in f:
            ip, port = line.strip().split(':')
            if port in ip_port_dict:
                ip_port_dict[port].append(ip)
            else:
                ip_port_dict[port] = [ip]
    return ip_port_dict

# Creates a directory and generates individual text files for each port with the corresponding IP addresses
def create_port_files(ip_port_dict, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    for port, ips in ip_port_dict.items():
        sorted_ips = sorted(ips, key=ip_sort_key)
        file_name = f"{folder}/port{port}.txt"
        with open(file_name, 'w') as f:
            for ip in sorted_ips:
                f.write(f"{ip}\n")

if __name__ == "__main__":
    readline.set_completer_delims(' \t\n')
    readline.parse_and_bind("tab: complete")
    
    file_path = input("Enter the path to the IP:Port list file: ")
    ip_port_dict = read_file(file_path)

    folder = "ports"
    create_port_files(ip_port_dict, folder)

    print(f"Port files have been created in the '{folder}' directory.")