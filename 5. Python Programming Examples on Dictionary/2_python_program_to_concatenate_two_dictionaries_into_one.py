"""
Problem Statement :  Python program to concatenate two dictionaries into one
"""

d1 = {1 : "One", 2 : "Two", 3 : "Three"}
d2 = {4 : "Four", 5 : "Five"}

# Concatenating two dictionary by using update() method.
d1.update(d2)

print ("Concatenated dictionary:")
print (d1)
