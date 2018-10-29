"""
Problem Statement : Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
"""
a = int(raw_input("Enter the value 'a':"))
b = int(raw_input("Enter the value 'b':"))

a = a + b
print "a = a + b = ", a
b = a - b
print "b = a - b = ", b
a = a - b
print "a = a - b = ", a

print "a = ", a, "b = ", b
