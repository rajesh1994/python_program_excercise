"""
Problem Statement : Python Program to Compute Simple Interest Given all the Required Values
"""

print ("Python Program to Compute Simple Interest Given all the Required Values:\n")
p = int(input("Enter a value for 'principle':"))
t = int(input("Enter a value for 'time' in years:"))
r = float(input("Enter a value for 'rate of interest':"))

roa = (p * t * r) / 100 # rate of annual return
pmi = roa / 12 # pmi -- per month interest
pdi = pmi / 30 # pdi -- per day interest
print ("\nThe interest for (one year) given values as follow:", round(roa,2))
print ("The interest for one month as follow:", round(pmi,2))
