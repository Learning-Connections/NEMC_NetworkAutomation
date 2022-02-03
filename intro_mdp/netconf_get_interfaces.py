#!/usr/bin/env python
# """Module docstring."""

# Imports
from ncclient import manager
import xmltodict
import xml.dom.minidom

# Constants
# Define our lab instance of csr1000v
csr100v = {
    "host": "192.168.0.122",
    "username": "cisco",
    "password": "C1$c0123",
    "netconf_port": 830,
    "ssh_port": 22
}

# Create an XML filter for targeted NETCONF queries
netconf_filter = """
 <filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
     <interface></interface>
   </interfaces>
 </filter>"""

# Global Variables
"""Global Variables Definitions"""

# Functions
"""no functions"""

# Open a connection using the manager object. 
with manager.connect(
    host=csr100v["host"],
    port=csr100v["netconf_port"],
    username=csr100v["username"],
    password=csr100v["password"],
    hostkey_verify=False
) as m:

# With the active connection, the <get-config> operation is executed, including the filter
# as you can see we target the data store 'running' to get the interfaces config
# netconf_reply represents the rpc-reply from the devic

   netconf_reply = m.get_config(source='running', filter=netconf_filter)

# let's print out the raw XML in a "pretty" fashion

   print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# now we convert the raw XML to a Python Ordered Dictionary that can be easily manipulated

   netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

# Create a list of interfaces
   interfaces = netconf_data["interfaces"]["interface"]

# we loop over the interfaces, printing out the interface names and status.
   for interface in interfaces:
     print("Interface {} enabled status is {}".format(
             interface["name"],
             interface["enabled"]
             )
         )

exit()
