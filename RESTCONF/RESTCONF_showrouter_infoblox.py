import requests
import json

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def printBytesAsJSON(bytes):
    print(json.dumps(json.loads(bytes), indent=2))


response = requests.get(
    url='https://127.0.0.1/restconf/data/Cisco-IOS-XE-native:native/router',
    auth=('admin', 'Infoblox'),
    headers={'Accept': 'application/yang-data+json'},
    verify=False)

# Pretty print our JSON response
printBytesAsJSON(response.content)


# Infoblox DDI API Request to display current networks

# requests.packages.urllib3.disable_warnings()
# url = "https://infoblox/wapi/v2.10.3/network?"
# response = requests.request("GET", url, auth=(
#     'david', 'Automation1!'), verify=False)
# print(response.text)
