"""
Problem Statement : Python Program to Find the Sum of First N Natural Numbers
"""

"""
Natural Numbers:
    A natural number is a number that occurs commonly and obviously in nature. As such, it is a whole, non-negative number. 
    
    The set of natural numbers, denoted N, can be defined in either of two ways:
        N = {0, 1, 2, 3, ...}
        N = (1, 2, 3, 4, ...}
    
    The set N, whether or not it includes zero, is a denumerable set. Denumerability refers to the fact that, even though there might be an infinite number of elements in a set, those elements can be denoted by a list that implies the identity of every element in the set.
    
    For example, it is intuitive from either the list {1, 2, 3, 4, ...} or the list {0, 1, 2, 3, ...} that 356,804,251 is a natural number, but 356,804,251.5, 2/3, and -23 are not.
"""

print ("Problem Statement : Python Program to Find the Sum of First N Natural Numbers:")

n = int(input("Enter a number:"))

sum1 = 0
while n > 0:
    sum1 = sum1 + n
    n = n - 1
print ("The sum of the first n natural numbers is", sum1)
