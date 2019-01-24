"""
Problem Statement : Python program to reverse a string without using recursion
"""

"""
Problem Solution:
1. Take a string from the user.
2. Use string slicing to reverse the string.
3. Print the reversed string.
4. Exit.
"""

string = input("Enter a string: ")
reversed_string = string[::-1]
print ("Reversed string:")
print (reversed_string)
