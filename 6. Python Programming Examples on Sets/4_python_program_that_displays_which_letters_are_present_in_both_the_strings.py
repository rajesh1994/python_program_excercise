"""
Problem Statement : Python program that displays which letters are present in both the strings
"""

string1 = input("Enter a string1: ")
string2 = input("Enter a string2: ")
a = list(set(string1)|set(string2))

print ("Letters present in both the strings are:")
for i in a:
    print (i)
