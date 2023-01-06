import socket

def find_websites(ip):
  # Perform a reverse DNS lookup to get the domain name
  domain = socket.gethostbyaddr(ip)[0]

  # Find the IP address for the domain name
  server_ip = socket.gethostbyname(domain)

  # Check if the IP address of the domain matches the input IP
  if server_ip == ip:
    print(f"{domain} is hosted on the same server as {ip}")
  else:
    print(f"{domain} is NOT hosted on the same server as {ip}")

# Test the function
find_websites("8.8.8.8")  # google.com
find_websites("104.16.35.3")  # cloudflare.com
find_websites("192.168.1.1")  # local network IP
