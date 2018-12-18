"""
Problem Statement : Python program to find the LCM of Two numbers using recursion
"""

"""
Problem Solution
1. Take two numbers from the user.

2. Initialize the multiple variable with the maximum value among two given numbers.

3. Check whether the multiple variable clearly divides both the number or not.

4. If it does, then end the process and return the multiple as the LCM.

5. If multiple doesn’t clearly divides both given numbers then increment the multiple by the max values among both the given numbers.

6. Return the multiple variable and print the LCM of the two variables.

7. Exit.
"""

def lcm(a, b):
    lcm.multiple = lcm.multiple + b
    if (lcm.multiple % a == 0 and lcm.multiple % b == 0):
        return lcm.multiple
    else:
        lcm(a, b)
        return lcm.multiple
lcm.multiple = 0
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if (a > b):
    LCM = lcm(b, a)
else:
    LCM = lcm(a, b)
print (LCM)
