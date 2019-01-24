"""
Problem Statement : Python program to find the sum of digits in a number without recursion
"""

"""
Problem Solution
1. Take a number from the user.
2. Using a while loop, obtain each digit and append it to the list.
3. Use the sum() function to obtain the sum of digits in the list.
4. Exit.
"""

n = int(input("Enter a number: "))
l = []
while(n > 0):
    dig = n % 10
    l.append(dig)
    n = n // 10
print ("The sum of digits are: ")
print (sum(l))
