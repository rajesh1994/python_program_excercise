"""
Problem Statement : Python Program to Find the Sum of Cosine Series
"""

import math
print ("Problem Statement : Python Program to Find the Sum of Cosine Series:")

def cosine(x, n):
    cosx = 1
    sinx = -1
    for i in range(2, n, 2):
        pi = 3.14
        # Converting degrees to radians
        y = x * (pi/180)
        cosx = cosx + (sinx*(y**i))/math.factorial(i)
        sinx = -sinx
    return cosx
x = int(input("Enter the value of x in degrees: "))
n = int(input("Enter the number of terms: "))
print (round(cosine(x,n),2))
