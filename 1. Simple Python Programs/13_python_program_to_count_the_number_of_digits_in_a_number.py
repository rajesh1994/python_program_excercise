"""
Problem Statement :  Python Program to Count the Number of Digits in a Number
"""

n = int(raw_input("Enter a number:"))
count = 0

while n > 0:
    count = count + 1
    #print count
    n = n / 10
    #print n
print "The number of digits in a number is %d." %count
