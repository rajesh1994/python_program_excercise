"""
Problem Statement : Python Program to Check if a Number is a Prime Number
"""

"""
Note:
Prime Numbers:
    A prime number is a whole number greater than 1 whose only factors are 1 and itself.
    A factor is a whole numbers that can be divided evenly into another number. The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.
    
Composite Numbers:
    Numbers that have more than two factors are called composite numbers.
"""
print ("Problem Statement : Python Program to Check if a Number is a Prime Number")
n = int(input("Enter a number:"))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print ("The entered number is a 'Composite Number'.")
            print (i, "times", n//i, "is", n,".")
            break
    else:
        print ("The entered number is a 'Prime Number'.")
else:
    print ("The entered number is a 'Composite Number'.")
