"""
Problem Statement : Python Program to Find the Second Largest Number in a List
"""

print ("Problem Statement : Python Program to Find the Second Largest Number in a List")

n = int(input("Enter number of elements: "))
l1 = []

for i in range(0, n):
    l2 = int(input("Enter a number:"))
    l1.append(l2)
sorted_list = sorted(l1)

print ("Second largest element in the list is", sorted_list[-2],".")
