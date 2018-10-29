"""
Poblem Statement : Python Program to Find the Sum of Digits in a Number
"""

print "Poblem Statement : Python Program to Find the Sum of Digits in a Number"
n = int(raw_input("Enter the value 'n':"))
sum = 0
while n > 0:
    dig = n % 10
    #print dig
    sum = sum + dig
    n = n // 10
print sum
