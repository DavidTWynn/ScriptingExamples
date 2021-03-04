#!/bin/python3
import napalm
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Script for running show lldp neighbors on Juniper, IOS, IOS-XR, and NXOS.

junos_driver = napalm.get_network_driver('junos')

junos_device = junos_driver(
    hostname='r2', username='cisco', password='cisco')
junos_device.open()
print("Junos device output\n")
print(junos_device.get_lldp_neighbors())
junos_device.close()

ios_driver = napalm.get_network_driver('ios')

ios_device = ios_driver(
    hostname='dsw1', username='cisco', password='cisco')
ios_device.open()
print("\n" + "=" * 81 + "\n\nIOS device output\n")
print(ios_device.get_lldp_neighbors())
ios_device.close()

iosxr_driver = napalm.get_network_driver('iosxr')

iosxr_device = iosxr_driver(
    hostname='core1', username='cisco', password='cisco')
iosxr_device.open()
print("\n" + "=" * 81 + "\n\nIOS-XR device output\n")
print(iosxr_device.get_lldp_neighbors())
iosxr_device.close()

nxos_driver = napalm.get_network_driver('nxos')

nxos_device = nxos_driver(
    hostname='172.17.1.7', username='cisco', password='cisco')
nxos_device.open()
print("\n" + "=" * 81 + "\n\nNXOS device output\n")
print(nxos_device.get_lldp_neighbors())
nxos_device.close()
