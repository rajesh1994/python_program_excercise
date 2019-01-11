"""
Problem Statement : Python program to find the power of a number using recursion
"""
"""
Problem Solution
1. Take the base and exponential value from the user.
2. Pass the numbers as arguments to a recursive function to find the power of the number.
3. Give the base condition that if the exponential power is equal to 1, return the base number.
4. If the exponential power isn’t equal to 1, return the base number multiplied with the power function called recursively with the arguments as the base and power minus 1.
5. Print the final result.
6. Exit.
"""
def power(n1, n2):
    if n2 == 1:
        return n2
    else:
        return n1 * power(n1, n2 - 1)
n1 = int(input("Enter the base value: "))
n2 = int(input("Enter the exponential value: "))
print ("The power of given numbers is ", power(n1, n2))
