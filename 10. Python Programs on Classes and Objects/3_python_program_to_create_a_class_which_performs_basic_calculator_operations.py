"""
Problem Statement : Python program to create a class which performs basic calculator operations
"""

"""
Problem Solution:

1. Create a class and using a constructor to initialize values of that class.
2. Create methods for adding, substracting, multiplying and dividing two numbers and returning the respective results.
3. Take the two numbers as inputs and create an object for the class passing the two numbers as parameters to the class.
4. Using the object, call the respective function depending on the choice taken from the user.
5. Print the final result.
6. Exit
"""

class cal:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def add(self):
		return self.a + self.b

	def sub(self):
		return self.a - self.b

	def mul(self):
		return self.a * self.b

	def div(self):
		return self.a / self.b

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
obj1 = cal(a, b)
choice = 1
while(choice != 0):
	print ("0. Exit")
	print ("1. Add")
	print ("2. Subtract")
	print ("3. Multiplication")
	print ("4. Division")
	choice = int(input("Enter your choice: "))
	if choice == 1:
		print ("Result:", obj1.add())
	elif choice == 2:
		print ("Result:", obj1.sub())
	elif choice == 3:
		print ("Result:", obj1.mul())
	elif choice == 4:
		print ("Result:", obj1.div())
	elif choice == 0:
		print ("Exiting!")
	else:
		print ("Invalid Choice!!")

