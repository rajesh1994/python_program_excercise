"""
Problem Statement : Python program to form a dictionary from an object of class
"""

class A(object):
    def __init__(self):
        self.A = 1
        self.B = 2
        self.C = 3
obj = A()
print (obj.__dict__)
