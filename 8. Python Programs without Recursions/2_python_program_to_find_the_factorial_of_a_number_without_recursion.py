"""
Problem Statement : Python program to find the factorial of a number without recursion
"""
"""
Factorial:

The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n.
For example, The value of 0! is 1, according to the convention for an empty product.

"""
"""
Problem Solution
1. Take a number from the user.
2. Initialize a factorial variable to 1.
3. Use a while loop to multiply the number to the factorial variable and then decrement the number.
4. Continue this till the value of the number is greater than 0.
5. Print the factorial of the number.
6. Exit.
"""

n = int(input("Enter a number to find the factorial : "))
fact = 1
while(n > 0):
    fact = fact * n
    n = n -1
print ("Factorial of the number is :", fact)
