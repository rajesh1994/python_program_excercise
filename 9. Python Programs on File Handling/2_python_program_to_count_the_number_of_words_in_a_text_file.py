"""
Problem Statement : Python program to count the number of words in a text file
"""

"""
Problem Solution:
1. Take the file name from the user.
2. Read each line from the file and split the line to form a list of words.
3. Find the length of items in the list and print it.
4. Exit.
"""

fname = str(input("Enter a file name with .txt extension: "))
num_words = 0
fopen = open(fname, 'r')
for i in fopen:
    words = i.split()
    num_words = num_words + len(words)
print ("Number of words:")
print (num_words)
