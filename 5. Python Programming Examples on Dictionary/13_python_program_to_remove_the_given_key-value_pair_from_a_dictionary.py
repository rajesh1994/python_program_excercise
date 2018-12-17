"""
Problem Statement : Python program to remove the given key-value pair from a dictionary
"""

d = {'Name' : 'Sam Paul', 'Gender' : 'M', 'Age' : 23, 'Color' : 'White'}
print ("Initial Dictionary:")
print (d)

input_key = input("Enter a key to delete a element from the dictionary: ")
if input_key in d:
    del d[input_key]
else:
    print ("The key not found!")
    exit(0)
print ("Updated dictionary:")
print (d)
