from netmiko import ConnectHandler

router_local = {"device_type": "cisco_ios",
          "ip": "192.168.100.66",
          "username" : "cisco",
          "port" : "22",
          "password": "cisco123!",
          }

net_connect = ConnectHandler(**router_local)
net_connect.enable()

command = "show ip int brief"

output = net_connect.send_command(command)
print("Output-ul comenzii '" + command + "' este:")
print(output)
