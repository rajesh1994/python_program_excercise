"""
Problem Statement : Python program to find the length of a list using recursion
"""

"""
Problem Solution:
1. Define a recursive function which takes a list as the argument.
2. Initialize a variable to a list.
3. In the function, put the condition that if it is not the original list, return 0.
4. Otherwise, recursively call the function to find the length of the list.
5. Print the final result of the string.
6. Exit.
"""

def length(list1):
    if not list1:
        return 0
    return 1 + length(list1[1::2]) + length(list1[2::2])
list1 = [1, 2, "Python", {"Name" : "Steve Trevor"}]
print ("Length of the list is:", length(list1))
