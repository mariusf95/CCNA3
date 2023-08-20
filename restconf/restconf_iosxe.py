from textwrap import indent
import requests
import json
from pprint import pprint

# set up connection parameters in a dictionary
router_devnet = {"ip": "sandbox-iosxe-recomm-1.cisco.com", "port": "443",
          "user": "developer", "password": "C1sco12345"}
router_local = {"ip": "192.168.100.66", "port": "443",
          "user": "cisco", "password": "cisco123!"}

# set REST API headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}
# print(url)
lista_rutere = [router_local]
for router in lista_rutere:
    url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"
    response = requests.get(url, headers=headers, auth=(router['user'], router['password']), verify=False)
    api_data = response.json()
    pprint (api_data)
    print("/" * 20)
    print(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["name"])
    print(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["ipv4"])
    print(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["bia-address"])
    print(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
    print("/" * 20)
    if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
        print('Interface is up')
