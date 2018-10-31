"""
Note:
If the sum of factorial of the digits in any number is equal the given number then the number is called as STRONG number.

Ex=1! +4! +5!= 1+24+120 = 145
"""
"""
Problem Statement :   Python Program to Check if a Number is a Strong Number
"""

print ("Problem Statement :   Python Program to Check if a Number is a Strong Number")

sum1 = 0
n = int(input("Enter a number:"))
temp = n
while n:
    i = 1
    f = 1
    r = n % 10
    while i <= r:
        f = f * i
        i = i + 1
    sum1 = sum1 + f
    n = n // 10
if sum1 == temp:
    print ("The number is a Strong Number.")
else:
    print ("The number is not a Strong Number")
