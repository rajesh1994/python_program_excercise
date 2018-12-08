"""
Problem Statement : Python program to count the number of vowels present in a string using sets
"""

string = input("Enter a string: ")
count = 0
vowels = ('aeiou')

for i in string:
    if i in vowels:
        count = count + 1
print ("Count of the vowels is:")
print (count)
