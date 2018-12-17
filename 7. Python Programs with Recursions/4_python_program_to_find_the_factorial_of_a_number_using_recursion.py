"""
Problem Statement : Python program to find the factorial of a number using recursion
"""

"""
Problem Solution
1. Take a number from the user and store it in a variable.

2. Pass the number as an argument to a recursive factorial function.

3. Define the base condition as the number to be lesser than or equal to 1 and return 1 if it is.

4. Otherwise call the function recursively with the number minus 1 multiplied by the number itself.

5. Then return the result and print the factorial of the number.

6. Exit.
"""

def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)
num = int(input("Enter a number: "))
print ("Factorial of %d is:" %num)
print (fact(num))
