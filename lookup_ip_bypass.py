import subprocess

def scan_server(server_ip):
    # Use the nmap command to scan the server for open ports
    cmd = ['nmap', '-p', '1-65535', server_ip]
    output = subprocess.run(cmd, capture_output=True).stdout.decode()
    
    # Parse the output to get the IP addresses of active devices
    active_ips = []
    for line in output.split('\n'):
        if 'Nmap scan report for' in line:
            ip = line.split(' ')[4]  # Get the IP address from the line
            active_ips.append(ip)
    
    return active_ips

# Get the server IP address from the user
server_ip = input('Enter the server IP address: ')

# Scan the server for active IP addresses
active_ips = scan_server(server_ip)

# Print the active IP addresses
print('Active IP addresses:')
for ip in active_ips:
    print(ip)
