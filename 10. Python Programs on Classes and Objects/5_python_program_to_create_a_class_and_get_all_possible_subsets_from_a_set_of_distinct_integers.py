"""
Problem Statement : Python program to create a class and get all possible subsets from a set of distinct integers
"""

"""
Problem Solution:

1. Create a class and define two methods in the class.
3. Method f1 is used to pass an empty list and the sorted list taken from the user to method f2.
4. Method f2 is used to compute all possible subsets of the list.
5. Then the result is returned from the function and printed.
6. Exit
"""

class sub:  
    def f1(self, s1):  
        return self.f2([], sorted(s1))  
 
    def f2(self, curr, s1):  
        if s1:  
            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])  
        return [curr]  
a=[]
n=int(input("Enter number of elements of list: "))
for i in range(0,n):
    b=int(input("Enter element: "))
    a.append(b)
print("Subsets: ")
print(sub().f1(a))
