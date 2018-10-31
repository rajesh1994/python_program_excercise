"""
Note:
Pascal's Triangle is a triangle of numbers where each number is the two numbers directly above it added together (except for the edges, which are all "1").
"""

"""
Problem Statement :  Python Program to Print the Pascal’s triangle for n number of rows given by the user
"""

print ("Problem Statement :  Python Program to Print the Pascal’s triangle for n number of rows given by the user")

n = int(input("Enter a value for number of rows:"))
l1 = []
for i in range(0, n):
    l1.append([])
    l1[i].append(1)
    for j in range(1, i):
        l1[i].append(l1[i - 1][j - 1] + l1[i - 1][j])
    if n != 0:
        l1[i].append(1)
for i in range(n):
    print(" "*(n-i),end = " ",sep=" ")
    for j in range(0, i + 1):
        print('{0:6}'.format(l1[i][j]),end=" ",sep=" ")
    print()
