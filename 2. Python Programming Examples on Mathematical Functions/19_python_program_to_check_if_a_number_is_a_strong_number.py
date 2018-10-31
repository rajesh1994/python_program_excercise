"""
    Note : A Polynomial can be expressed in terms that only have positive integer exponents and the operations of addition, subtraction, and multiplication.
    
    In other words, it must be possible to write the expression without division.
    
    Examples of Polynomials:
    x^2 + 2x +5 --- Since all of the variables have integer exponents that are positive this is a polynomial.

    5x^-2 +1 --- Not a polynomial because a term has a negative exponent

    3x½ +2 --- Not a polynomial because a term has a fraction exponent

"""

"""
Problem Statement :   Python Program to Check if a Number is a Strong Number
"""

print ("Problem Statement :   Python Program to Check if a Number is a Strong Number")

import math

print ("Enter the co-efficients of the form ax^3+bx^2+cx+d")
l1 = []
for i in range(0, 4):
    a = int(input("Enter Co-efficients: "))
    l1.append(a)

x = int(input("Enter a value for 'x': "))
sum1 = 0
j = 3

for i in range(0, 3):
    while j > 0:
        sum1 = sum1 + (l1[i] * math.pow(x, j))
        break
    j = j - 1
sum1 = sum1 + l1[3]
print ("The value of the polynimial is:", sum1)
