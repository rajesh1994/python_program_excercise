"""
Problem Statement : Python program to flatten a list without using recursion
"""

"""
Problem Solution
1. A variable must be initialized with a nested list.
2. Use a lambda function and map() to map the flatten function to each element in the nested list to flatten the list.
3. Print the flattened list.
4. Exit.
"""

l = [[1, 2, 3], ["India", "UAE"]]
flatten = lambda n: sum(map(flatten, n), []) if isinstance(n, list) else [n]
print (flatten(l))
