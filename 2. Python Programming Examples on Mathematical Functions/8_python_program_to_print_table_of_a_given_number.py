"""
Problem Statement : Python Program to Print Table of a Given Number
"""

print ("Problem Statement : Python Program to Print Table of a Given Number:")

n = int(input("Enter a number:"))
for i in range(0, 16):
    print (i, "x", n, "=", i * n)
