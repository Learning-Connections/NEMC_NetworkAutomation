#!/usr/bin/env python
# """Module docstring."""

"""parsingJSON.py
imports, parsin JSON into data structure and files example
"""
# Imports
import json
from pprint import pprint

# Constants
"""no constants"""

# Global Variables
"""Global Variables Definitions"""
my_file = "interface-hands-on.json"


# Functions
def read_from_file():
    """This is the same code of parsingJSON.py but inside a function"""
    # Read in the JSON text
    with open(my_file, 'r') as f:
        json_text = f.read()
        # Display the type and contents of the json_text variable
        print("json_text is a", type(json_text))
        print(json_text)

        # Use the json module to parse the JSON string into native Python data
        json_data = json.loads(json_text)

        # Display the type and contents of the json_data variable
        print("json_data is a", type(json_data))
        pprint(json_data)
        return json_data


def modify_interface_name(jdata):
    
    if_name = input("New Interface Name: [{}]".format(jdata["ietf-interfaces:interface"]["name"])) or jdata["ietf-interfaces:interface"]["name"]
    jdata["ietf-interfaces:interface"]["name"] = if_name
    print("The new interface configuration is: \n")
    pprint(jdata)
    return jdata


def modify_interface_descr(jdata):
    if_descr = input("New Interface Description: ")
    jdata["ietf-interfaces:interface"]["description"] = if_descr
    print("The new interface configuration is: \n")
    pprint(jdata)
    return jdata


def modify_ip_mask(jdata):
    if_ip = input("New IP Address: ")
    if_netmask = input("Net Netmask: ")
    ip_mask = {"ip": if_ip, "netmask": if_netmask}
    jdata["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0] = ip_mask
    print("The new interface configuration is: \n")
    pprint(jdata)
    return jdata


def save_to_file(jdata):
    try:
        with open(my_file, 'w') as f:
            json.dump(jdata, f, indent=4)
    except:
        print("unable to write the file!")


def menu():
    """Menu Funtion with conditional loop"""
    s = None
    json_data = {}
    while s != '0':
        print('**** MENU ****')
        print('1. Read JSON from file')
        print('2. Modify Interface name')
        print('3. Modify Interface desc')
        print('4. Modify Interface IP and Netmask')
        print('5. Save to JSON file')
        print('0. Exit')
        s = input('Type your choice: ')
        if s == '1':
            json_data = read_from_file()
        elif s == '2':
            json_data = modify_interface_name(json_data)
        elif s == '3':
            json_data = modify_interface_descr(json_data)
        elif s == '4':
            json_data = modify_ip_mask(json_data)
        elif s == '5':
            save_to_file(json_data)
        elif s == '0':
            quit()
        else:
            print("Select a valid option...")


def main():
    menu()


# check if this is the main script and execute it
if __name__ == '__main__':
    main()
