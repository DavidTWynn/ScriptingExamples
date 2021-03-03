#!/bin/python3
import paramiko
import getpass
import time
import subprocess

devices = {
    'r1': {
        'ip': '127.0.0.1',
    },
    'r3': {
        'ip': '127.0.0.1'
    }
}

user = "cisco"
password = "cisco"
command = "show ip int b\n"


def get_connection(ip, user, password):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=ip, username=user, password=password, look_for_keys=False)
    return ssh


for device in devices.keys():
    print(f"Executing on device: {devices[device]['ip']}\n\n")
    ssh = get_connection(
        ip=devices[device]['ip'], user=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.readlines()
    time.sleep(1)
    ssh.close
    formatted = (' '.join(map(str, output)))
    print(formatted)
    #proc = subprocess.Popen(["/bin/bash", "-c", "grep up | grep -v Loopback \
    #    | grep -v unassigned"], stdin=subprocess.PIPE)
    #proc.communicate(formatted.encode('utf-8'))
