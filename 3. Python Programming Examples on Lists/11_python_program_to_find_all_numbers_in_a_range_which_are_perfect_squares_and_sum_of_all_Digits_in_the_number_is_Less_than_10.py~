"""
Problem Statement : Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10
"""

"""
Perfect Number:
    A number made by squaring a whole number.

Example:
    16 is a perfect square because 4**2 = 16
    25 is also a perfect square because 5**2 = 25
"""
lrange = int(input("Enter the value for lower range: "))
urange = int(input("Enter the value for upper range: "))

a = [x for x in range(lrange, urange + 1) if (int(x ** 0.5) ** 2) == x and sum(list(map(int, str(x)))) < 10]
print ("Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10:")
print (a)
