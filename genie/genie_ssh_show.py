from netmiko import ConnectHandler
from pprint import pprint

router_devnet = {"device_type": "cisco_ios",
          "ip": "sandbox-iosxe-latest-1.cisco.com",
          "username" : "admin",
          "port" : "22",
          "password": "C1sco12345",
          }

router_local = {"device_type": "cisco_ios",
          "ip": "192.168.100.66",
          "username" : "cisco",
          "port" : "22",
          "password": "cisco123!",
          }

lista_rutere = [router_local,router_devnet]
for router in lista_rutere:
    commands = ["show ip interface brief", "show version"]
    print("Output for: " + router["ip"])
    for command in commands:
        with ConnectHandler(**router) as net_connect:
            output = net_connect.send_command(command, use_genie=True)
            print()
            pprint(output)
            print()
    print("-" * 80)





