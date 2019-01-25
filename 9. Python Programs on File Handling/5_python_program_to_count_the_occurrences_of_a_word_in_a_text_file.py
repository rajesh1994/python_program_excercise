"""
Problem Statement : Python program to count the occurrences of a word in a text file
"""

"""
Problem Solution
1. Take the file name and the word to be counted from the user.
2. Read each line from the file and split the line to form a list of words.
3. Check if the word provided by the user and any of the words in the list are equal and if they are, increment the word count.
4. Exit.
"""

fname = str(input("Enter a file name with .txt extension: "))
word = str(input("Enter a word to be searched: "))
fopen = open(fname, 'r')
count = 0
for i in fopen:
    words = i.split()
    for i in words:
        if i == word:
            count = count + 1
print ("Occurrences of a word is:")
print (count)
