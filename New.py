import socket

def check_site_available():
  # Get the IP address from the user
  ip_address = input("Enter an IP address: ")

  try:
    domain = socket.gethostbyaddr(ip_address)[0]
    print(f"Domain name for {ip_address}: {domain}")
  except socket.herror:
    print(f"No domain found for {ip_address}")

# Test the function by prompting the user to enter an IP address
check_site_available()
