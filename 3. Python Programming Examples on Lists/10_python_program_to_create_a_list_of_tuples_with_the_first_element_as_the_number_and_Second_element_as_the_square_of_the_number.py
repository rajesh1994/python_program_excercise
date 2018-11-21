"""
Problem Statement :  Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
"""

lrange = int(input("Enter the value for lower range: "))
urange = int(input("Enter the value for upper range: "))

a = [(x, x * x) for x in range(lrange, urange + 1)]
print ("\nList of Tuples with the First Element as the Number and Second Element as the Square of the Number:")
print (a)
