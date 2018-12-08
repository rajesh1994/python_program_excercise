"""
Problem Statement : Python program to generate a dictionary that contains numbers (between 1 and n) in the form (x,x*x)
"""

n = int(input("Enter the number: "))

d = {x : x * x for x in range(0, n + 1)}

print ("Dictionary sequence:")
print (d)
print ("Sum of all items in a dictionary:")
print (sum(d.values()))
