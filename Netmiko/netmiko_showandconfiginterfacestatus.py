from netmiko import ConnectHandler
import time

R1 = {
    'ip': '127.0.0.1',
    'username': 'cisco',
    'password': 'cisco',
    'device_type': 'cisco_ios',
}
print('Checking interface status..')
net_connect = ConnectHandler(**R1)

# output = net_connect.send_command('show ip int brie')
# print(output)

output = net_connect.send_command('show ip interface brief', use_textfsm=True)
# print(output)

name = output[4]['intf']
status = output[4]['status']
print('\nInterface ' + name + ' status is ' + status)

if status == 'up':
    print('\nFinishing the script')
else:
    print('Configuring no shutdown on the interface\n')
    config_commands = ['interface ' + name, 'no shut']
    output = net_connect.send_config_set(config_commands)
    print(output)
    print('\nFinished configuration change, verifying...')
    time.sleep(5)
    output = net_connect.send_command('show ip int brie', use_textfsm=True)
    name = output[4]['intf']
    status = output[4]['status']
    print('\nInterface ' + name + ' status is ' + status)
