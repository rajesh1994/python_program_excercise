"""
Problem Statement : Python Program to Print all Integers that Are not Divisible by Either 2 or 3 and Lie between 1 and 50
"""

print "Numbers are not divisible by either 2 or 3 and lie between 1 and 50:"
for i in range(0, 51):
    if i % 2 != 0 and i % 3 != 0:
        print i
