"""
Problem Statement : Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
"""

print ("Problem Statement : Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List:")

n = int(input("Enter a number:"))
l = []
for i in range(0, n):
    a = int(input("Enter a elements:"))
    l.append(a)
sum1 = 0
sum2 = 0
sum3 = 0
for j in l:
    if j > 0:
        if j % 2 == 0:
            sum1 = sum1 + j
        else:
            sum2 = sum2 + j
    else:
        sum3 = sum3 + j
print ("\nSum of all positive even numbers:", sum1)
print ("\nSum of all positive odd numbers:", sum2)
print ("\nSum of all negative numbers:", sum3)
