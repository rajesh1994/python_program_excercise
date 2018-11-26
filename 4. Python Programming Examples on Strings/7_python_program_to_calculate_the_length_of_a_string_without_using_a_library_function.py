"""
Problem Statement : Python program to calculate the length of a string without using a library function
"""

string = input("Enter the string: ")
length = 0
for i in string:
    length = length + 1
print ("Length of the given string is %d." %length)
