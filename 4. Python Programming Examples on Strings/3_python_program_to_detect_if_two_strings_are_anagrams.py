"""
Problem Statemnt : Python program to detect if two strings are anagrams
"""

"""
Anagram definition:
    An anagram is a word or phrase formed by rearranging the letters in another word or phrase.
"""

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if sorted(string1) == sorted(string2):
    print ("The strings are anagrams.")
else:
    print ("The strings are not anagrams.")
