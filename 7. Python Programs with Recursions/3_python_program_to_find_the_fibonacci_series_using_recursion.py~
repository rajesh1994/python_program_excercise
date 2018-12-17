"""
Problem Statement : Python program to find the fibonacci series using recursion
"""

"""
Problem Solution:
1. Take the number of terms from the user and store it in a variable.

2. Pass the number as an argument to a recursive function named fibonacci.

3. Define the base condition as the number to be lesser than or equal to 1.

4. Otherwise call the function recursively with the argument as the number minus 1 added to the function called recursively with the argument as the number minus 2.

5. Use a for loop and print the returned value which is the fibonacci series.

6. Exit.
"""

def fib(num):
    if num <= 1:
        return num
    else:
        return (fib(num -1) + fib(num - 2))
num = int(input("Enter a number: "))

print ("Fibonacci Sequence:")
for i in range(num):
    print fib(i)
