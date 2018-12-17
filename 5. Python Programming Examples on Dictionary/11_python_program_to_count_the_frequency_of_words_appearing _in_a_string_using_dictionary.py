"""
Problem Statement : Python program to count the frequency of words appearing  in a string using dictionary
"""

string = input("Enter a string: ")
l = []
l = string.split()
word_freq = [l.count(p) for p in l]

print (dict(zip(l, word_freq)))
