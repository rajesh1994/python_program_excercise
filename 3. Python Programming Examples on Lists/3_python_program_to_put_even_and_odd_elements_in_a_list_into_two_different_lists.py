"""
Problem Statement : Python Program to Put Even and Odd elements in a List into Two Different Lists
"""

print ("Problem Statement : Python Program to Put Even and Odd elements in a List into Two Different Lists")

n = int(input("Enter number of elements: "))
l1 = []

for i in range(0, n):
    l2 = int(input("Enter a number: "))
    l1.append(l2)
even_list = []
odd_list = []
for j in l1:
    if j % 2 == 0:
        even_list.append(j)
    else:
        odd_list.append(j)
print ("Odd element's list:", odd_list)
print ("Even element's list:", even_list)
