"""
Problem Statement : Python Program to Print all Numbers in a Range Divisible by a Given Number
"""

print "Problem Statement : Python Program to Print all Numbers in a Range Divisible by a Given Number"

lower = int(raw_input("Enter the lower limit value for range: "))
upper = int(raw_input("Enter the upper limit value for range: "))
n = int(raw_input("Enter the number to be divided by: "))

print "The following are divided by %d:" %n
for i in range(lower, upper+1):
    if i % n == 0:
            print i
