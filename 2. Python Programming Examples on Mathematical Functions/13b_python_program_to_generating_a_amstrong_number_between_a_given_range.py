"""
Note:

An Armstrong Number is a number that when you raise each digit of the number to the power of the number of digits and then add them up you get the original number.

a is a Armstrong Number if
𝑎=(𝑎1)𝑛+(𝑎2)𝑛...(𝑎𝑛)𝑛

For example 371 is an Armstrong Number because
371=33+73+1
"""

"""
Problem Statement : Python Program to Check if a Number is an Armstrong Number
"""

print ("Problem Statement : Python Program to Generating a Amstrong number between a given range")

n1 = int(input("Enter the starting range:"))
n2 = int(input("Enter the ending range:"))
print ("The following numbers are Armstrong numbers:")
for i in range(n1, n2):
    len_n = len(str(i))
    l1 = list(map(int,str(i)))
    l2 = list(map(lambda x : x ** len_n, l1))
    if (sum(l2) == i):
        print (i)
