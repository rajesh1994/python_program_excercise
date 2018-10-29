"""
Problem Statement : Python Program to Generate all the Divisors of an Integer
"""

print ("Python Program to Generate all the Divisors of an Integer:")

n = int(input("Enter a number:"))
print ("The divisors of the number %d are:" %n)
for i in range(1, n + 1):
    if n % i == 0:
        print (i)
