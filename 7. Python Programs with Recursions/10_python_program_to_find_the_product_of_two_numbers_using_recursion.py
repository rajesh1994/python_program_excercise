"""
Problem Statement : Python program to find the product of two numbers using recursion
"""
"""
Problem Solution
1. Take two numbers from the user.
2. Pass the numbers as arguments to a recursive function to find the product of the two numbers.
3. Give the base condition that if the first number is lesser than the second, recursively call the function with the arguments as the numbers interchanged.
4. If the second number isn’t equal to 0, again call the function recursively, else return 0.
5. Print the final product of the two numbers.
6. Exit.
"""
import sys
sys.setrecursionlimit(1500)
def product(n1, n2):
    if n1 < n2:
        return product(n2, n1)
    elif n1 != 0:
        return n1 + product(n1, n2 - 1)
    else:
        return 0
n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))
print ("The Product of two numbers: ", product(n1, n2))
