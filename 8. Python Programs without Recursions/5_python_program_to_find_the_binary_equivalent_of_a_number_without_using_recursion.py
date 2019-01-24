"""
Problem Statement : Python program to find the binary equivalent of a number without using recursion
"""

"""
Problem Solution
1. Take a number from the user.
2. Using a while loop, convert each digit into binary and append it to the list.
3. Reverse the list and using a for loop print the elements of the list.
4. Exit.
"""

n = int(input("Enter a number: "))
l = []
while(n > 0):
    dig = n % 2
    l.append(dig)
    n = n//2
l.reverse()
print ("Binary Equilent is: ")
for i in l:
    print (i, end = " ")
