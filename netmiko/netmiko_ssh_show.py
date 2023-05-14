from netmiko import ConnectHandler

router_devnet = {"device_type": "cisco_ios",
          "ip": "sandbox-iosxe-latest-1.cisco.com",
          "username" : "admin",
          "port" : "22",
          "password": "C1sco12345",
          }

router_local = {"device_type": "cisco_ios",
          "ip": "192.168.100.64",
          "username" : "student",
          "port" : "22",
          "password": "cisco",
          }

lista_rutere = [router_local,router_devnet]

for router in lista_rutere:
    net_connect = ConnectHandler(**router)
    net_connect.enable()
    commands = ["show run int Gig1", "show ip route", "show version | i uptime"]

    for i in commands:
        print("-" * 80)
        interface_cli = net_connect.send_command(i)
        print("Output-ul comenzii " + i + " este:")
        print(interface_cli)
