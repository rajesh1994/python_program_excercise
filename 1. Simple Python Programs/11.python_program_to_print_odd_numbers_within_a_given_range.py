"""
Problem Statement :  Python Program to Print Odd Numbers Within a Given Range
"""
print "Problem Statement :  Python Program to Print Odd Numbers Within a Given Range"
lower_limit = int(raw_input("Enter value for lower limit: "))
upper_limit = int(raw_input("Enter value for upper limit: "))
for i in range(lower_limit, upper_limit + 1):
    if i % 2 != 0:
        print i
