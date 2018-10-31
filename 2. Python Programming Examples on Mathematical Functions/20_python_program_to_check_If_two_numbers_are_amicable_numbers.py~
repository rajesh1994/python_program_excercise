"""
Note:
    Amicable numbers are pairs of numbers, each of which is the sum of the others aliquot divisors.
    
    Example, 220 and 284 are amicable numbers whereas all the aliquot divisors of 220, i.e., 110, 55, 44, 22, 10, 5, 4, 2, 1 add up to 284 and all the aliquot divisors of 284, i.e., 142, 71, 4, 2, 1 add up to 220.
"""

"""
Problem Statement :   Python Program to Check If Two Numbers are Amicable Numbers
"""

print ("Problem Statement :   Python Program to Check If Two Numbers are Amicable Numbers")

n1 = int(input("Enter a number1:"))
n2 = int(input("Enter a number2:"))
t1 = n1
t2 = n2
l1 = []
l2 = []
for i in range(1, n1):
    if n1 % i == 0:
        l1.append(i)
for j in range(1, n2):
    if n2 % j == 0:
        l2.append(j)
#print ("l1 = ", l1)
#print ("l2 = ",  l2)
#print ("Sum(l1) = ", sum(l1))
#print ("Sum(l2) = ",  sum(l2))
if sum(l1) == t2 and sum(l2) == t1:
    print ("The given numbers are 'Amicable Numbers'.")
else:
    print ("The given numbers are not 'Amicable Numbers'.")
