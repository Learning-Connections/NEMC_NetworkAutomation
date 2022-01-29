name = input("What's your name? \n")

print ("Hello {}, nice to meet you!".format(name))
print ('"name" is a {} type of variable'.format(type(name)))
print ('The attributes and methods of a {string} are:\n {obj}'.format(string=type(name), obj=dir(name)))
