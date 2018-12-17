"""
Problem Statement : Python program to determine how many times a given letter occurs in a string recursively
"""

def check(string, char):
    if not string:
        return 0
    elif string[0] == char:
        return 1 + check(string[1:], char)
    else:
        return check(string[1:], char)
string = input("Enter a string: ")
char = input("Enter a character: ")
print ("The given letter present in",check(string, char),"times.")
