"""
Problem Statement : Python program to find the GCD of two numbers using recursion
"""

"""
Problem Solution
1. Take two numbers from the user.

2. Pass the two numbers as arguments to a recursive function.

3. When the second number becomes 0, return the first number.

4. Else recursively call the function with the arguments as the second number and the remainder when the first number is divided by the second number.

5. Return the first number which is the GCD of the two numbers.

6. Print the GCD.

7. Exit.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print ("GCD of two numbers using recursion:")
print (gcd(a, b))
