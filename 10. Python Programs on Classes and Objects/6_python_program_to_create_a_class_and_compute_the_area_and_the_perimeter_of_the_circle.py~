"""
Problem Statement : Python program to create a class and compute the area and the perimeter of the circle
"""

"""
Problem Statement:

Problem Solution
1. Take the value of radius from the user.
2. Create a class and using a constructor initialise values of that class.
3. Create a method called as area which returns the area of the class and a method called as perimeter which returns the perimeter of the class.
4. Create an object for the class.
5. Using the object, call both the methods.
6. Print the area and perimeter of the circle.
7. Exit
"""

import math
class circle():
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
        
    def perimeter(self):
        return 2 * math.pi * self.radius
        
radius = int(input("Enter the radius of the circle: "))
obj = circle(radius)
print ("Area of the circle:", round(obj.area(),2))
print ("Perimeter of the circle:", round(obj.perimeter(),2))
