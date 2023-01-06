import subprocess

def get_dns_records(ip_address):
    # Use the nslookup command to get the DNS records for the server
    cmd = ['nslookup', ip_address]
    output = subprocess.run(cmd, capture_output=True).stdout.decode()
    
    # Parse the output to get the domain names
    domain_names = []
    for line in output.split('\n'):
        if 'name = ' in line:
            domain_name = line.split(' = ')[1]
            domain_names.append(domain_name)
    
    return domain_names

# Test the function
ip_address = '192.0.2.1'  # Replace this with the IP address you want to search for
print(get_dns_records(ip_address))
