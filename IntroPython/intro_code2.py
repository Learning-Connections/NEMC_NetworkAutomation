#intro_code2.py
#conditional (if, elif, else) and functions


def check_age(age):
    if age < 14:
        return "You cannot drive yet, keep walking! :)"
    elif age >14 and age <18:
        return "You can drive a scooter!"
    else:
        return "You can drive a car now!"

name = input("What's your name?\n")
print ("Hello {}, nice to meet you".format(name))
age = input("How old are you?\n")
check=check_age(int(age))
print (check)