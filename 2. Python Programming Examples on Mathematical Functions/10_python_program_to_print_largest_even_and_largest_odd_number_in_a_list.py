"""
Problem Statement : Python Program to Print Largest Even and Largest Odd Number in a List
"""

print ("Problem Stateent : Python Program to Print Largest Even and Largest Odd Number in a List")

n = int(input("Enter the number of elements to be in the list:"))
l1 = []
for i in range(0, n):
    a = int(input("Enter a element:"))
    l1.append(i)
l2 = []
l3 = []
for j in l1:
    if j % 2 == 0:
        l2.append(j)
    else:
        l3.append(j)
l2.sort()
l3.sort()
print ("Even element's list:", l2)
print ("Odd element's list:", l3)
print ("Largest even number from the list is",l2[-1])
print ("Largest odd number from the list is",l3[-1])
