"""
Problem Statement : Python Program to Sort the List According to the Second Element in Sublist
"""

print ("Problem Statement : Python Program to Sort the List According to the Second Element in Sublist")

l1 = [['a', '33'], ['b', '22'], ['c', '11']]

for i in range(0, len(l1)):
    for j in range(0, len(l1)-i-1):
        if l1[j][i] > l1[j + 1][1]:
            temp = l1[j]
            l1[j] = l1[j + 1]
            l1[j + 1] = temp
print ("Sorting the List According to the Second Element in Sublist is", l1)
