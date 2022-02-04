#!/usr/bin/env python
# """Module docstring."""

# Imports
import requests
import json

# Constants
# Define our lab instance of csr1000v
csr100v = {
    "host": "192.168.0.122",
    "username": "cisco",
    "password": "C1$c0123",
    "restconf_port": 433,
}
# Global Variables
"""Global Variables Definitions"""

# Functions


def get_interfaces():
   # Create an XML filter for targeted NETCONF queries
    url = "https://{}:{}/restconf/data/ietf-interfaces:interfaces".format(
        csr100v["host"], csr100v["restconf_port"])
    print(url)


def add_loopback():
    # Create an XML configuration template for ietf-interfaces
    netconf_interface_template = """
   <config>
       <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
           <interface>
               <name>{name}</name>
               <description>{desc}</description>
               <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                   {type}
               </type>
               <enabled>{status}</enabled>
               <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                   <address>
                       <ip>{ip_address}</ip>
                       <netmask>{mask}</netmask>
                   </address>
               </ipv4>
           </interface>
       </interfaces>
   </config>"""
    # Ask for the Interface Details to Add
    new_loopback = {}
    new_loopback["name"] = "Loopback" + input("What loopback number to add? ")
    new_loopback["desc"] = input("What description to use? ")
    new_loopback["type"] = IETF_INTERFACE_TYPES["loopback"]
    new_loopback["status"] = "true"
    new_loopback["ip_address"] = input("What IP address? ")
    new_loopback["mask"] = input("What network mask? ")
    # Create the NETCONF data payload for this interface
    netconf_data = netconf_interface_template.format(
        name=new_loopback["name"],
        desc=new_loopback["desc"],
        type=new_loopback["type"],
        status=new_loopback["status"],
        ip_address=new_loopback["ip_address"],
        mask=new_loopback["mask"]
    )
    # Open a connection using the manager object.
    with manager.connect(
        host=csr100v["host"],
        port=csr100v["netconf_port"],
        username=csr100v["username"],
        password=csr100v["password"],
        hostkey_verify=False
    ) as m:
        # send the data to the device
        netconf_reply = m.edit_config(netconf_data, target='running')
        # Print out the raw XML that returned
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


def remove_loopback():
     # Create an XML configuration template for ietf-interfaces
    netconf_interface_template = """
   <config>
       <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
           <interface operation="delete">
           	<name>{name}</name>
           </interface>
       </interfaces>
   </config>"""

    # Ask for the Interface Details to Add
    delete_loopback = {}
    delete_loopback["name"] = "Loopback" + \
        input("What loopback number to delete? ")

    # Create the NETCONF data payload for this interface
    netconf_data = netconf_interface_template.format(
        name=delete_loopback["name"]
    )
    


def save_config():
    # Create an XML body to execute the save operation
    save_body = """
   <cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
   """
    


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
        # elif s=='2':
        #  add_loopback()
        # elif s=='3':
        #  remove_loopback()
        # elif s=='4':
        #  save_config()
        elif s == '0':
             quit()
        else:
             print("Select a valid option...")


def main():
    menu()


# check if this is the main script and execute it
if __name__ == '__main__':
    main()
