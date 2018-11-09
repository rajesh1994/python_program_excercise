"""
Problem Statement : Python Program to Determine all Pythagorean Triplets in the Range
"""
"""
Pythagorean Triple:

    A "Pythagorean Triple" is a set of positive integers, a, b and c that fits the rule:
    a2 + b2 = c2
    
    Example: The smallest Pythagorean Triple is 3, 4 and 5.
    
    Let's check it:

    32 + 42 = 52

    Calculating this becomes:

    9 + 16 = 25

    Yes, it is a Pythagorean Triple!
"""
print ("Problem Statement : Python Program to Determine all Pythagorean Triplets in the Range")

ulimit = int(input("Enter a value for 'Upper Limit': "))
c = 0
m = 2

while c < ulimit:
    for n in range(1, m + 1):
        a = m * m -n * n
        b = 2 * m * n
        c = m * m + n * n
        if c > ulimit:
            break
        if a == 0 or b == 0 or c == 0:
            break
        print (a, b, c)
    m = m + 1        
