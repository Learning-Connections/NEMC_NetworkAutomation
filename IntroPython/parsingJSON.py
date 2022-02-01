#!/usr/bin/env python
# """Module docstring."""

"""parsingJSON.py
imports, parsin JSON into data structure and files example
"""
#Imports
import json
from pprint import pprint

#Constants
"""no constants"""

#Global Variables
"""Global Variables Definitions"""
my_file="interface-config.json"


#Functions
def main():
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

#check if this is the main script and execute it
if __name__ == '__main__':
        main()