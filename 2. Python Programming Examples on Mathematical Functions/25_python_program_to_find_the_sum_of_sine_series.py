"""
Problem Statement : Python Program to Find the Sum of Sine Series
"""
import math
print ("Problem Statement : Python Program to Find the Sum of Sine Series:")

def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi = 22/7
        # Converting degrees to radians
        y = x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine
x = int(input("Enter a value of x in degrees: "))
n = int(input("Enter the number of terms: "))
print (round(sin(x,n),2))
