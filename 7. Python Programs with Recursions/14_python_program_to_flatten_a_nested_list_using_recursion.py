"""
Problem Statement : Python program to flatten a nested list using recursion
"""

"""
Problem Solution
1. Initialize a variable to a nested list.
2. Pass the list as an argument to a recursive function to flatten the list.
3. In the function, if the list is empty, return the list.
4. Otherwise call the function is recursively with the sublists as the parameters until the entire list is flattened.
5. Print the flattened list.
6. Exit.
"""

def flatten(nlist):
    if len(nlist) == 0:
        return nlist
    if isinstance(nlist[0], list):
        return flatten(nlist[0]) + flatten(nlist[1:])
    return nlist[:1] + flatten(nlist[1:])
nlist = [[1, 2], [3, 4], [5, 6]]
print ("Flatten list is:", flatten(nlist))

"""
Note:
Python isinstance()
The isinstance() function checks if the object (first argument) is an instance or subclass of classinfo class (second argument).
"""
