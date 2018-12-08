"""
Problem Statement : Python program to count the occurrences of each word in a given string sentence
"""

string = input("Enter the string: ")
word = input("Enter the word: ")
count = 0
l = []
a = string.split(" ")

for i in range(0, len(a)):
    if word == a[i]:
        count = count + 1
print ("Count of the word is:")
print (count)
