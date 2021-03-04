# Repo of scripts for learning and tinkering with

Compilation of scripts for working with Cisco and Juniper network gear using Paramiko, Netmiko, and Napalm. 

## Getting Started

```
sudo apt install pip
pip install netmiko
```

### Prerequisites

You will need access to a lab, linux, and Python3. These were tested on Ubuntu 20.04.

## Installation	

git clone https://github.com/DavidTWynn/ScriptingExamples.git

## Troubleshooting

```
pip list | grep netmiko    -- Check for netmiko
pip list | grep paramiko   -- Check for paramiko
python3			   -- Verify the import of netmiko and paramiko
from netmiko import ConnectHandler
import paramiko
```

## Resources

Nemiko supported platforms - https://ktbyers.github.io/netmiko/PLATFORMS.html

NTC-Templates that parse what netmiko gets to Python lists - https://github.com/networktocode/ntc-templates/tree/master/templates

TextFSM - https://github.com/google/textfsm

Paramiko tutorial - https://blog.wimwauters.com/networkprogrammability/2020-03-23-paramiko_introduction_part1/

Good video on paramiko and netmiko - https://www.youtube.com/watch?v=_c2zOspIaYA

Paramiko Github - https://github.com/paramiko/paramiko
