"""
Note:
A perfect number: a number is perfect when the sum of its divisors (except the number itself) equals the given number.

6 : The divisors of 6 are 1,2,3 & 6. To show that this is a perfect number we could all the divisors except the number itself
1+2+3 = 6
"""

"""
Problem Statement :   Python Program to generate a perfect number between the given range
"""

print ("Problem Statement :   Python Program to generate a perfect number between the given range")

n1 = int(input("Enter a value for lower range:"))
n2 = int(input("Enter a value for upper range:"))
for r in range(n1, n2):
