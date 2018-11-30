"""
Problem Statement : Python program to take in two strings and display the larger string without using built-in functions
"""

string1 = input("Enter the string1: ")
string2 = input("Enter the string2: ")
count1 = 0
count2 = 0

for i in string1:
    count1 = count1 + 1

for j in string2:
    count2 = count2 + 1

if count1 == count2:
    print ("Both strings are equal.")
elif count1 > count2:
    print ("String1 is larger.")
else:
    print ("String2 is largers.")
