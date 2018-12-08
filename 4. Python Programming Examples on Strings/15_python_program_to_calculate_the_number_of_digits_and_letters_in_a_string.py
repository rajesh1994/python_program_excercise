"""
Problem Statement : Python program to calculate the number of digits and letters in a string
"""

string = input("Enter the string:")
d_count = 0
l_count = 0

for i in string:
    if i.isdigit():
        d_count = d_count + 1
    l_count = l_count + 1

print ("The number of digits is:")
print (d_count)
print ("The number of characters is:")
print (l_count)
