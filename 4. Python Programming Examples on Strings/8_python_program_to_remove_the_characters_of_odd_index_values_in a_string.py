"""
Problem Statement : Python program to remove the characters of odd index values in a string
"""

def with_out_odd_index(string):
    final = ""
    for i in range(len(string)):
        if i % 2 == 0:
            final = final + string[i]
    return final
string = input("Enter the string: ")
print ("Modified string:")
print (with_out_odd_index(string))
