"""
Problem Statement : Python program to find all numbers which are odd and palindromes between a range of numbers without using recursion
"""

"""
Problem Solution:
1. Take a upper limit and lower limit from the user.
2. Using list comprehension, store all the numbers in the list that are odd and palindromes.
3. Print the list.
4. Exit.
"""
a = []
llimit = int(input("Enter the value for Lower limit: "))
ulimit = int(input("Enter the value for Upper limit: "))
range1 = range(llimit, ulimit)
a = [x for x in range(llimit, ulimit + 1) if x % 2 == 1 and str(x) == str(x)[::-1]]
print ("The numbers which are odd & palindrome between a range of numbers:")
print (a)
