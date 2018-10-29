"""
Problem Statement : Python Program to Read Two Numbers and Print Their Quotient and Remainder
"""

print "Problem Statement : Python Program to Read Two Numbers and Print Their Quotient and Remainder"

a = int(raw_input("Enter value 1: "))
b = int(raw_input("Enter value 2: "))

remainder = a % b
quotient = a / b

print "The remainder for %d/%d is " %(a,b), remainder
print "The quotient for %d/%d is " %(a,b), quotient
