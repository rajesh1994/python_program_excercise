"""
Problem Statement : Python program to find the binary equivalent of a number recursively
"""

"""
Problem Solution
1. Define a recursive function which takes a number as the argument.

2. Take a number from the user and pass it as an argument to a recursive function.

3. In the function, put the base condition that if the number is zero, return the formed list.

4. Otherwise, convert each digit into binary and append it to the list.

5. Reverse the list and using a for loop print the elements of the list.

6. Exit.
"""

l = []

def convert(n):
    if n == 0:
        return l
    else:
        d = n % 2
        l.append(d)
        convert(n//2)
a = int(input("Enter a number: "))
convert(a)

print ("Binary equivalent:")
for i in l:
    print (i, end = " ")
