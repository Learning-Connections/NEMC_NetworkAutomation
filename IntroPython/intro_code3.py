#!/usr/bin/env python
# """Module docstring."""

"""intro_code3.py
Data Types, Loops: iterative and conditional, Python Structure,  Files
"""
#Imports
"""nothing to import"""

#Constants
"""no constants"""

#Global Variables
"""Global Variables Definitions"""
my_file="intro_code3.txt"

#Functions
def read_from_file(file):
    """Read from file example"""
    try:
        with open (file, mode='r') as f:
            text=f.read()
            if len(text)>0:
                return text
            else: 
                print("File is empty!")
    except: print("Unable to open the file!")

def add_text():
    t=input("Add text: ")
    return t+"\n"

def save_to_file(file, text):
    """Save to a text file example"""
    try:
        with open (file, 'a') as f:
            f.write(text)
    except:
        print("Unable to save!")

def menu():
    """Menu Funtion with conditional loop"""
    s=None
    text=''
    while s!='0':
        print ('**** MENU ****')
        print('1. Read from file')
        print('2. Add text')
        print('3. Save to file')
        print('0. Exit')
        s=input ('Type your choice: ')
        if s=='1':
            text=read_from_file(my_file)
            print(text)
        elif s=='2':
            text=add_text()
            print (text)
        elif s=='3':
            save_to_file(my_file, text)
        elif s=='0':
            quit()
        else:
            print("Select a valid option...")

def main():
    menu()

#check if this is the main script and execute it
if __name__ == '__main__':
        main()
