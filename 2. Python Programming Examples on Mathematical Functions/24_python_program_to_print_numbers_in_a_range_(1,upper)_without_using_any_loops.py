"""
Problem Statement : Python Program to Print Numbers in a Range (1,upper) Without Using any Loops
"""

print ("Problem Statement : Python Program to Print Numbers in a Range (1,upper) Without Using any Loops:")

def num(upper):
    if upper > 0:
        num(upper - 1)
        print (upper)
upper = int(input("Enter a value for upper range: "))
num(upper)
