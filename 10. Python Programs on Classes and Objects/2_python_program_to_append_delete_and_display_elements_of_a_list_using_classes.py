"""
Problem Statement : Python program to append, delete and display elements of a list using classes
"""

"""
Problem Solution:

1. Create a class and using a constructor initialize values of that class.
2. Create methods for adding, removing and displaying elements of the list and return the respective values.
3. Create an object for the class.
4. Using the object, call the respective function depending on the choice taken from the user.
5. Print the final list.
6. Exit
"""

class list1():
	def __init__(self):
		self.n = []

	def add(self, a):
		return self.n.append(a)

	def remove(self, b):
		return self.n.remove(b)

	def dis(self):
		return self.n
obj1 = list1()
choice = 1
while choice != 0
	print ("0. Exit")
	print ("1. Add")
	print ("2. Delete")
	print ("3. Display")

