"""
Problem Statement : Python program to find the area of a rectangle using classes
"""

"""
Problem Solution:

1. Take the value of length and breadth from the user.
2. Create a class and using a constructor initialise values of that class.
3. Create a method called as area and return the area of the class.
4. Create an object for the class.
5. Using the object, call the method area() with the parameters as the length and breadth taken from the user.
6. Print the area.
7. Exit
"""
class rectangle():
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	def area(self):
		return self.length * self.breadth
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
object1 = rectangle(length, breadth)
method_call = object1.area()
print ("Area of the rectangle is:", method_call)
