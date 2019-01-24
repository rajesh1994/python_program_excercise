"""
Problem Statement : Python program to read the contents of a file
"""
"""
Problem Solution:
1. Take the file name from the user.
2. Use readline() function for the first line first.
3. Use a while loop to print the first line and then read the remaining lines and print it till the end of file.
4. Exit.
"""

fname = str(input("Enter the name of the file with .txt extension: "))
fopen = open(fname, 'r')
line = fopen.readline()
while(line!=""):
    print (line)
    line = fopen.readline()
fopen.close()
