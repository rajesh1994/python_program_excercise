"""
Problem Statement : Python Program to Find the LCM of Two Numbers
"""

print ("Problem Statement : Python Program to Find the LCM of Two Numbers")

n1 = int(input("Enter a value1:"))
n2 = int(input("Enter a value2:"))
if n1 < n2:
    min1 = n1
else:
    min1 = n2
while(1):
    if min1 % n1 == 0 and min1 % n2 == 0:
        print ("LCM is:", min1)
        break
    min1 = min1 + 1
