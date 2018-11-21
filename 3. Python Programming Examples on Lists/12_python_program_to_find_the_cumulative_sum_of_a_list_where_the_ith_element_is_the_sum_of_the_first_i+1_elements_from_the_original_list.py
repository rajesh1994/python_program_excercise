"""
Problem Statement : Python program to find the cumulative sum of a list where the ith element is the sum of the first i+1 elements from the original list
"""

l1 = []
n = int(input("Enter the number of elements in the list:"))

for i in range(0, n):
    l2 = int(input("Enter element" + str(i + 1) + ":"))
    l1.append(l2)

l3 = [sum(l1[0: i + 1]) for i in range(0, len(l1))]
print ("The original list is:", l1)
print ("The new list is:", l3)
