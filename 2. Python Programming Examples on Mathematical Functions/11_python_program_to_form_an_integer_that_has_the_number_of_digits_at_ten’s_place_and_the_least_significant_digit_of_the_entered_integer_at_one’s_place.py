"""
Problem Statement :  Python Program to Form an Integer that has the Number of Digits at Ten’s Place and the Least Significant Digit of the Entered Integer at One’s Place
"""

print ("Problem Stateent :  Python Program to Form an Integer that has the Number of Digits at Ten’s Place and the Least Significant Digit of the Entered Integer at One’s Place")

n = int(input("Enter a number:"))
temp = n
k = 0
while n > 0:
    k = k + 1
    n = n // 10
a = str(temp)
b = str(k)
c = b + a[k-1]
print ("The new number formed:", int(c))
