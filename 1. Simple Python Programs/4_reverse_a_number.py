"""
Problem Statement : Python Program to Reverse a Given Number
"""
print "Problem Statement : Python Program to Reverse a Given Number"
n = int(raw_input("Enter the value 'n':"))
rev = 0
while n > 0:
    dig = n % 10
    #print "dig = ", dig
    rev = rev * 10 + dig
    #print "rev = ", rev
    n = n//10
    #print n
print "The reversed value of n is:", rev
