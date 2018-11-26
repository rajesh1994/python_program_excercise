"""
Problem Statement : Python program to replace all occurrences of ‘a’ with $ in a string
"""

string = input("Enter a string: ")
m_string = string.replace('a', '$')
m_string = m_string.replace('A', '$')

print ("Modified String:")
print (m_string)
