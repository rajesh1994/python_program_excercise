"""
Problem Statement : Python program to count the number of lines in a text file
"""

"""
Problem Solution:
1. Take the file name from the user.
2. Read each line from the file and increment the count variable
3. Print the line count.
4. Exit.
"""
num_lines = 0
fname = str(input("Enter a file name with .txt extension: "))
fopen = open(fname, 'r')
for i in fopen:
    num_lines = num_lines + 1
print ("The number of the lines in text file is:", num_lines)
