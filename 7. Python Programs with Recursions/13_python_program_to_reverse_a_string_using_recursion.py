"""
Problem Statement : Python program to reverse a string using recursion
"""

"""
Problem Solution:
1. Take a string from the user.
2. Pass the string as an argument to a recursive function to reverse the string.
3. In the function, put the base condition that if the length of the string is equal to 0, the string is returned.
4. Otherwise recursively call the reverse function to slice the part of the string except the first character and concatenate the first character to the end of the sliced string.
5. Print the reversed string.
6. Exit.
"""

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
string = input("Enter a String: ")
print ("The reversed string :", reverse(string))
