"""
Problem Statement : Python Program to Read a Number n and Compute n+nn+nnn
"""
print "Problem Statement : Python Program to Read a Number n and Compute n+nn+nnn"

n = int(raw_input("Enter the value 'n':"))

str1 = str(n)

nn = str1 + str1

nnn = str1 + str1 + str1

int1 = int(nn) + int(nnn)

sum = n + int1

print "The value of n+nn+nnn = ", sum
