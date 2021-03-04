#!/bin/python3
from ncclient import manager
from jinja2 import Template

m = manager.connect(host='172.17.1.1', username='cisco',
                    password='cisco', device_params={'name': 'csr'})

interface_filter = '''
  <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <interface>
            <GigabitEthernet>
              <name>1</name>
            </GigabitEthernet>
          </interface>
      </native>
  </filter>
'''

result = m.get_config('running', interface_filter)
print(result)

# SCHEMA = m.get_schema('Cisco-IOS-XE-lldp')
# print(SCHEMA)
