"""
Problem Statement : Python program to count number of lowercase & uppercase characters in a string
"""

string1 = input("Enter the string: ")
string2 = string1
count1 = 0
count2 = 0

for i in string1:
    if i.islower():
        count1 = count1 + 1
print ("The number of lowercase characters in the string is:")
print (count1)

for j in string2:
    if j.isupper():
        count2 = count2 + 1
print ("The number of uppercase characters in the string is:")
print (count2)
