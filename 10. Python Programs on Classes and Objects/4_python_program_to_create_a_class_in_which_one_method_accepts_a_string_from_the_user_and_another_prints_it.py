"""
Problem Statement : Python program to create a class in which one method accepts a string from the user and another prints it
"""

"""
Problem Solution:

1. Create a class and using a constructor initialize values of that class.
3. Create two methods called as get which takes in the value of a string and another called put that prints the string.
4. Create an object for the class.
5. Using the object, call both the methods.
6. The string is printed.
7. Exit
"""

class print1():
	def __init__(self):
		self.string = ""
	def get(self):
		self.string = input("Enter a string: ")
	def put(self):
		print("String is: ")
		print (self.string)
obj1 = print1()
obj1.get()
obj1.put()
"""
class print1():
    def __init__(self):
        self.string=""
 
    def get(self):
        self.string=input("Enter string: ")
 
    def put(self):
        print("String is:")
        print(self.string)
 
obj=print1()
obj.get()
obj.put()
"""
