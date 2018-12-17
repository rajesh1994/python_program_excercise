"""
Problem Statement : Python program to find the sum of elements in a list recursively
"""

"""
Problem Solution
1. Define a recursive function which takes an array and the size of the array as arguments.

2. Declare an empty list and initialize it to an empty list.

3. Consider a for loop to accept values for the list.

4. Take the number of elements in the list and store it in a variable.

5. Accept the values into the list using another for loop and insert into the list.

6. Pass the list and the size of the list as arguments to the recursive function.

7. If the size of the list is zero, return 0.

8. Otherwise return the sum of the last element of the list along with the recursive function call (with the size reduced by 1).

9. The returned value is stored in a variable and the final sum is printed.

10. Exit.
"""

def sum_array(array, soz):
    
