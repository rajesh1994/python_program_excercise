"""
Problem Statement : Python program to read a string from the user and append it into a file
"""

"""
Problem Solution:
1. Take the file name from the user.
2. Open the file in append mode.
2. Take in a string from the user, append it to the existing file and close the file.
3. Open the file again in read mode and display the contents of the file.
4. Exit.
"""

fname = str(input("Enter a file name with .txt extention: "))
fopen = open(fname, 'a')
ustring = str(input("Enter a string to append: "))
fwrite1 = fopen.write("\n")
fwrite2 = fopen.write(ustring)
fopen.close()
fname1 = str(input("Enter a file name with .txt extention: "))
fopen1 = open(fname1, 'r')
fread = fopen1.read()
print (fread)
