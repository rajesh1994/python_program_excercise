"""
Problem Statement : Python Program to Read Height in Centimeters and then Convert the Height to Feet and
Inches
"""
print ("Python Program to Read Height in Centimeters and then Convert the Height to Feet and Inches")
height_cm = int(input("Enter your height in centi meters:"))

# 1 cm = 0.393701 inches
height_i = height_cm * 0.393701
# 1 cm = 0.0328084 feet
height_f = height_cm * 0.0328084

print ("The height in inches", round(height_i,2))
print ("The height in feets", round(height_f,2))
