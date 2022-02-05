#!/usr/bin/env python
# """Module docstring."""

# Imports
from math import fabs
from textwrap import indent
import requests
import json

# Constants
# Define our lab instance of csr1000v
csr1000v = {
    "host": "192.168.0.122",
    "username": "cisco",
    "password": "C1$c0123",
    "restconf_port": 443,
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

auth = requests.auth.HTTPBasicAuth(
    csr1000v["username"], csr1000v["password"])
# Global Variables
"""Global Variables Definitions"""

# Functions


def get_interfaces():
   # Create an XML filter for targeted NETCONF queries
    module = "ietf-interfaces:interfaces"
    url = "https://{}:{}/restconf/data/{}".format(
        csr1000v["host"], csr1000v["restconf_port"], module)
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=headers, auth=auth, verify=False)
    print("The HTTP Response code is: {}\n".format(response.status_code))
    print("The JSON Response is:")
    print(response.json())
    print("\n\n")


def add_loopback():
    module = "ietf-interfaces:interfaces"
    url = "https://{}:{}/restconf/data/{}".format(
        csr1000v["host"], csr1000v["restconf_port"], module)
    auth = requests.auth.HTTPBasicAuth(
        csr1000v["username"], csr1000v["password"])
    payload = {
        "interface": [
            {
                "name": "Loopback100",
                "description": "Added with RESTCONF",
                "type": "iana-if-type:softwareLoopback",
                "enabled": "true",
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": "172.16.100.1",
                            "netmask": "255.255.255.0"
                        }
                    ]
                }
            }
        ]
    }
    # response = requests.get(url, headers=headers, auth=requests.auth.HTTPBasicAuth(csr1000v["username"], csr1000v["password"]),verify=False)
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url, headers=headers,
                             data=json.dumps(payload), auth=auth, verify=False)

    if (response.status_code == 201):
        print("Successfully added interface")
    else:
        print("Issue with adding interface")


def remove_loopback():
    module = "ietf-interfaces:interfaces/interface=Loopback100"
    url = "https://{}:{}/restconf/data/{}".format(
        csr1000v["host"], csr1000v["restconf_port"], module)
    auth = requests.auth.HTTPBasicAuth(
        csr1000v["username"], csr1000v["password"])

    requests.packages.urllib3.disable_warnings()
    response = requests.delete(url, headers=headers, auth=auth, verify=False)

    if (response.status_code == 204):
        print("Successfully deleted interface")
    else:
        print("Issue with deleting interface")


def save_config():
    module = 'cisco-ia:save-config'
    url = "https://{}:{}/restconf/data/{}".format(
        csr1000v["host"], csr1000v["restconf_port"], module)
    auth = requests.auth.HTTPBasicAuth(
        csr1000v["username"], csr1000v["password"])
    requests.packages.urllib3.disable_warnings()
    response = requests.post(url, headers=headers, auth=auth, verify=False)
    print(response)
    if (response.status_code == 200):
        print("Successfully saved config")
    else:
        print("Issue with saving config")

def menu():
    """Menu Funtion with conditional loop"""
    s = None
    text = ''
    while s != '0':
        print('**** MENU ****')
        print('1. Get interfaces')
        print('2. Add loopback')
        print('3. Remove loopback')
        print('4. Save Config ')
        print('0. Exit')
        s = input('Type your choice: ')
        if s == '1':
            get_interfaces()
        elif s == '2':
            add_loopback()
        elif s=='3':
            remove_loopback()
        elif s=='4':
            save_config()
        elif s == '0':
            quit()
        else:
            print("Select a valid option...")


def main():
    menu()


# check if this is the main script and execute it
if __name__ == '__main__':
    main()
