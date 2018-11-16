"""
Problem Statement : Python Program to Find the Second Largest Number in a List Using Bubble Sort
"""

print ("Problem Statement : Python Program to Find the Second Largest Number in a List Using Bubble Sort")

n = int(input("Enter the number of elements:"))
l1 = []
for i in range(0, n):
    l2 = int(input("Enter a element:"))
    l1.append(l2)
for i in range(0, len(l1)):
    for j in range(0, len(l1) -i - 1):
        if l1[j] > l1[j + 1]:
            temp = l1[j]
            l1[j] = l1[j + 1]
            l1[j + 1] = temp
print ("Second largest number is", l1[n - 1])
