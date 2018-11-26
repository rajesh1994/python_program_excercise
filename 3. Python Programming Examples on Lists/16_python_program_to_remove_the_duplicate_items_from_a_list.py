"""
Problem Statement : Python program to remove the duplicate items from a list
"""

l1 = []
n = int(input("Enter the number of elements in the list:"))

for i in range(0, n):
    l2 = int(input("Enter an element" + str(i+1) + ":"))
    l1.append(l2)
u_list = []
for j in l1:
    if j not in u_list:
        u_list.append(j)
print ("Non Duplicate items of the list:")
print (u_list)
