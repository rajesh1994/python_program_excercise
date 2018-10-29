"""
Problem Statement : Accept Three Digits and Print all Possible Combinations from the Digits
"""
print "Problem Statement : Accept Three Digits and Print all Possible Combinations from the Digits"
n1 = int(raw_input("Enter first number: "))
n2 = int(raw_input("Enter second number: "))
n3 = int(raw_input("Enter third number: "))
l = []
l.append(n1)
l.append(n2)
l.append(n3)
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if i != j and j != k and k != i:
                print l[i], l[j], l[k]
