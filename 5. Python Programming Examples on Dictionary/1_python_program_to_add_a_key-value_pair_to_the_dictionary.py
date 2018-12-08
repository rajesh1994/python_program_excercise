"""
Problem Statement : Python program to add a key-value pair to the dictionary
"""

key = int(input("Enter the key(int) to be added: "))
value = input("Enter the value for key to be added: ")
d = {}
d.update({key:value})

print ("The updated dictionary is:")
print (d)
