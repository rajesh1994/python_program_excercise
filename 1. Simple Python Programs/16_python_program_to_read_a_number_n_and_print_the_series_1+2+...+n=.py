"""
Problem Statement : Python Program to Read a Number n And Print the Series 1+2+...+n= 
"""
print "Problem Statement : Python Program to Read a Number n And Print the Series '1+2+...+n='"
n = int(raw_input("Enter a number: "))
a = []
for i in range(0, n + 1):
    a.append(i)
ans = sum(a)
if n == 0:
    print "0", " = ", ans
elif n == 1:
    print "0 + 1", " = ", ans
elif n == 2:
    print "0 + 1 + 2", " = ", ans
else:
    print "0 + 1 + 2 + ... + %d" %n, " = ", ans
