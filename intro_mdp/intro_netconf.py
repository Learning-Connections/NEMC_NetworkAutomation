#!/usr/bin/env python
# """Module docstring."""

#Imports
from ncclient import manager

#Constants
#Define our lab instance of csr1000v
csr100v = {
    "host": "192.168.0.122",
    "username": "cisco",
    "password": "C1$c0123",
    "netconf_port": 830,
    "ssh_port": 22
}

#Global Variables
"""Global Variables Definitions"""

#Functions
"""no functions"""

#Open a connection using the manager object.

m = manager.connect(
   host=csr100v["host"],
   port=csr100v["netconf_port"],
   username=csr100v["username"],
   password=csr100v["password"],
   hostkey_verify=False
   )

#Review the capabilities of the device by looping over the server_capabilities property of the manager object.

for capability in m.server_capabilities:
   print(capability)

#close the connection to the device to end the NETCONF session.

m.close_session()
exit()