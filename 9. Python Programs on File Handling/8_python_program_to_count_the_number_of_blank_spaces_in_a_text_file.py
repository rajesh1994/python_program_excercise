"""
Problem Statement : Python program to count the number of blank spaces in a text file
"""

"""
Problem Solution:
1. Take the file name from the user.
2. Read each line from the file and split the line to form a list of words.
3. Use a for loop to traverse through the words in the list and another for loop to traverse through the letters in the word.
4. Check if the letter is a space and if it is, increment the variable count.
5. Print the final count of the number of spaces.
6. Exit.
"""
count = 0
fname = str(input("Enter a filename with .txt extension: "))
fopen = open(fname,"r")
for line in fopen:
    words = line.split()
    for i in words:
        for letter in i:
            if (letter.isspace):
                count = count + 1
print ("Occurance of the blank spaces: ")
print (count)
