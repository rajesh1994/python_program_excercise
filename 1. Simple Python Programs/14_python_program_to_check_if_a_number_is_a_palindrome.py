"""
Problem Statement :  Python Program to Check if a Number is a Palindrome
"""

n = int(raw_input("Enter a number: "))
temp = n
rev = 0
while n > 0:
    dig = n % 10
    print dig
    rev = rev * 10 + dig
    #print rev
    n = n / 10
if temp == rev:
    print "The number is a Palindrome."
else:
    print "The number is not a Palindrome."
