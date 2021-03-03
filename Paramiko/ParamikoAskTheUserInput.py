#!/bin/python3
import paramiko
import getpass
import datetime as dt
import time

devices = {
    'r1': {
        'ip': '127.0.0.1',
        'name': 'R1',
    },
    'r3': {
        'ip': '127.0.0.1',
        'name': 'R3',
    }
}

user = input("Username: ")
password = getpass.getpass()
command = input("Enter command to execute: ")


def get_connection(ip, user, password):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=ip, username=user, password=password, look_for_keys=False)
    return ssh


right_now = dt.datetime.now()
print(f"Time ran: {right_now:%I:%M %p on %m/%d/%y}\n" + "=" * 81)


for device in devices.keys():
    print("\n" + f"Executing on {devices[device]['name']}:\
 {devices[device]['ip']}\n\n" + "=" * 81)
    try:
        ssh_conn = get_connection(
            ip=devices[device]['ip'], user=user, password=password)
        stdin, stdout, stderr = ssh_conn.exec_command(command)
        output = stdout.readlines()
        formatted = (' '.join(map(str, output)))
        print(formatted)
        ssh_conn.close
        time.sleep(1)
        print("\n" + "=" * 81)
    except Exception as e:
        print(e, "Check the Username, Password, and IP reachability.")
        break
print("\n" + "Done processing script." + "\n")
