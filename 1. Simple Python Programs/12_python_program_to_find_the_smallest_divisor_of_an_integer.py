"""
Problem Statement :  Python Program to Find the Smallest Divisor of an Integer
"""

print "Problem Statement :  Python Program to Find the Smallest Divisor of an Integer"
n = int(raw_input("Enter an integer: "))
#print "The divider is ", n
l = []

for i in range(2, n + 1):
    if n % i == 0:
        l.append(i)
l.sort()
print "The smallest divisor is", l[0]
