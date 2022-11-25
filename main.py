import requests
import os
from get_ipaddress import get_ipaddress_ipinfo

ips = get_ipaddress_ipinfo()

# Default allow outgoing and deny incoming

os.system("ufw default deny incoming")
os.system("ufw default allow outgoing")
os.system("ufw allow ssh")

for ip in ips:

    os.system("ufw allow proto tcp from {} to any port 443,80".format(ip))
