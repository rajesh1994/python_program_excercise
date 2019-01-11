"""
Problem Statement : Python program to find if a number is prime or not prime using recursion
"""

"""
Problem Solution:

1. Take a number from the user.
2. Pass the number as an argument to a recursive function and initialize the divisor count to NULL.
3. Then check the number of divisors of the number using recursion and either True or False is returned.
4. The final result is printed.
5. Exit.
"""
def prime(n, div = None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print ("Not a Prime Number")
            return False
        else:
            return prime(n, div-1)
    else:
        print ("Number is Prime")
        return True        
n = int(input("Enter a number:"))
prime(n)
