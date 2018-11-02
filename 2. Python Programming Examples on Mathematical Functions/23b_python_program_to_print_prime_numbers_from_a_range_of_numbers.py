"""
Problem Statement : Python Program to print Prime Numbers from a range of numbers
"""

print ("Python Program to print Prime Numbers from a range of numbers:")

n1 = int(input("Enter a lower range number: "))
n2 = int(input("Enter a upper range number: "))
print ("The following numbers are Prime Numbers:")
for n3 in range(n1, n2):
    if n3 > 1:
        for n4 in range(2, n3):
            if n3 % n4 == 0:
                break
        else:
            print (n3)
