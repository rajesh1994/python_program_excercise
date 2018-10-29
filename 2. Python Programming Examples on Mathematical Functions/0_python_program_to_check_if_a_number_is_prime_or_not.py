"""
Problem Statement : Python Program to Check If a number is Prime or not
"""

print ("Problem Statement : Python program to check if a number is Prime or not:")
n = int(input("Enter a number:"))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print (n, "is not a prime number.")
            break
    else:
        print (n, "is a prime number.")
else:
    print (n, "is not a prime number.")
