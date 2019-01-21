"""
Problem Statement : Python program to find the total sum of a nested list using recursion
"""

"""
Problem Solution
1. Initialize a variable to a nested list.
2. Pass the list as an argument to a recursive function to find the sum of elements of the list.
3. In the function, use a for loop and recursion to obtain the elements inside the sublists and store the summed up elements in a variable.
4. Return the total sum of the elements.
5. Print the sum of the nested list.
6. Exit.
"""

def sum1(nlist):
    total = 0
    for i in nlist:
        print (i)
        if type(i) == type([]):
            total = total + sum1(i)
        else:
            total = total + i
    return total
nlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print ("The sum is:", sum1(nlist))
