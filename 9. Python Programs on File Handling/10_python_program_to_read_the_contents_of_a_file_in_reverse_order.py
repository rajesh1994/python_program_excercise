"""
Problem Statement : Python program to read the contents of a file in reverse order
"""

"""
Problem Solution:
1. Take the file name from the user.
2. Read each line from the file using for loop and store it in a list.
3. Print the elements of list in reverse order.
4. Exit.
"""

fname = str(input("Enter a file name with .txt extension: "))
fopen = reversed(list(open(fname, 'r')))
for line in fopen:
	print (line.rstrip())
