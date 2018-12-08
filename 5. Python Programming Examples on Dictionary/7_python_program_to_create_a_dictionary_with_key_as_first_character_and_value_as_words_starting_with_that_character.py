"""
Problem Statement : Python program to create a dictionary with key as first character and value as words starting with that character
"""

string = input("Enter a string: ")
d = {}
l = string.split()

for word in l:
    if word[0] not in d.keys():
        d[word[0]] = []
        d[word[0]].append(word)
    else:
        if word not in d[word[0]]:
            d[word[0]].append(word)
for k, v in d.items():
    print (k, ":", v)
