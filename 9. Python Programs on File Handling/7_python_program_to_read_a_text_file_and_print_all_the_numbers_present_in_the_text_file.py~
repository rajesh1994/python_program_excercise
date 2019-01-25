"""
Problem Staement : Python program to read a text file and print all the numbers present in the text file
"""

"""
Problem Solution
1. Take the file name from the user.
2. Read each line from the file and split the line to form a list of words.
3. Use a for loop to traverse through the words in the list and another for loop to traverse through the letters in the word.
3. Check if the letter provided by the user is a digit and if it is, print it.
4. Exit.
"""
fname = str(input("Enter a filename with .txt extension: "))
fopen = open(fname, 'r')
for line in fopen:
    words = line.split()
    for i in words:
        for letter in i:
            if letter.isdigit():
                print (letter)
