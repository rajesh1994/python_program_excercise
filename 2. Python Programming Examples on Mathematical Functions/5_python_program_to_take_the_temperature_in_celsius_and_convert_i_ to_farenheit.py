"""
Problem Statement : Python Program to Take the Temperature in Celsius and Convert it to Farenheit
"""

print ("Python Program to Take the Temperature in Celsius and Convert it to Farenheit:")
# Formula for Celsius to Farenheit conversion (0°C × 9/5) + 32 = 32°F

temp_c = float(input("Enter temperature in celsius:"))

temp_f = temp_c * (9/5) + 32

print ("The temperature in farenheight:", round(temp_f,2),"°F")
