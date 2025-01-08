import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print("Connecting via SSH => show version (filtered)")
#
from netmiko import ConnectHandler
### VAR

### EXEC
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="10.10.20.48",
    port="22",
    username="developer",
    password="C1sco12345"
    )
output=sshCli.send_command("show version")
for line in output.splitlines():
    if 'Cisco IOS Software' in line:
        ios_version = line.strip()
    elif 'uptime' in line:
        hostname = line.split()[0]
        sys_uptime = line    
    elif 'interface' in line:
        num_interfaces = line.split()[0]
print("IOS Version")
print(ios_version)
print("Hostname")
print(hostname)
print("System uptime")
print(sys_uptime)
print("Number of Interfaces")
print(num_interfaces)

