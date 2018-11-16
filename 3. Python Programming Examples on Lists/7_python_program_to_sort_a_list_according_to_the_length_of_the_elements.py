"""
Problem Statement : Python Program to Sort a List According to the Length of the Elements
"""

print ("Problem Statement : Python Program to Sort a List According to the Length of the Elements")

n = int(input("Enter the number of elements:"))
l1 = []

for i in range(0, n):
    l2 = input("Enter a element:")
    l1.append(l2)
l1.sort(key = len)
print (l1)
