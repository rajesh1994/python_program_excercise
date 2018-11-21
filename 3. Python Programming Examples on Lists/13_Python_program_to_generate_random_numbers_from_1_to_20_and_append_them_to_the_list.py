"""
Problem Statement : Python program to generate random numbers from 1 to 20 and append them to the list
"""

import random

l1 = []
n = int(input("Enter the number of elements in the list:"))

for i in range(n):
    l1.append(random.randint(1, 20))
print ("The randomized list is:", l1)
