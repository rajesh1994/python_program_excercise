"""
Problem Statement : Python program to form a new string made of the first 2 and last 2 characters from a given string
"""
string = input("Enter the string: ")
count = 0
for i in string:
 count = count + 1
n_string = string[0:2] + string[count - 2 : count]
print ("Newly formed string is:")
print (n_string)
