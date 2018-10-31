"""
Note:
A perfect number: a number is perfect when the sum of its divisors (except the number itself) equals the given number.

6 : The divisors of 6 are 1,2,3 & 6. To show that this is a perfect number we could all the divisors except the number itself
1+2+3 = 6
"""

"""
Problem Statement :   Python Program to Check if a Number is a Perfect Number
"""

print ("Problem Statement :   Python Program to Check if a Number is a Perfect Number")

n = int(input("Enter a number:"))
l1 = []
for i in range(1, n):
    if n % i == 0:
        l1.append(i)
        print (l1)
if sum(l1) == n:
    print ("The given number is a Perfect Number.")
else:
    print ("The given number is a Non Perfect Number.")
