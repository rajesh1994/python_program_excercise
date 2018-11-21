"""
Problem Statement : Python program to swap the first and last value of a list
"""

l1 = []
n = int(input("Enter the number of element in the list:"))

for i in range(0, n):
    l2 = int(input("Enter a value:"))
    l1.append(l2)
print ("The Actual list is:", l1)
temp = l1[0]
l1[0] = l1[-1]
l1[-1] = temp

print ("The swapped list is:", l1)
