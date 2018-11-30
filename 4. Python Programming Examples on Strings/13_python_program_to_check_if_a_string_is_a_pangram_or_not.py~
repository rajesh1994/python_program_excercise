"""
Problem Statement : Python program to check if a string is a pangram or not
"""

"""
Pangram:
    A sentence, verse, etc., that includes all the letters of the alphabet.
    
    Example : We promptly judged antique ivory buckles for the next prize
"""

from string import ascii_lowercase as asc_lwr

def check(s):
    return set(asc_lwr) - set(s.lower()) == set([])

string = input("Enter the string: ")

if check(string) == True:
    print ("The string is a pangram")
else:
    print ("The string is not a pangram")
