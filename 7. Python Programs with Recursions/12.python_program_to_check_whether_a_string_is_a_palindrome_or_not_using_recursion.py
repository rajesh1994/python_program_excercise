"""
Problem Statement : Python program to check whether a string is a palindrome or not using recursion
"""
"""
Problem Solution
1. Take a string from the user.
2. Pass the string as an argument to a recursive function.
3. In the function, if the length of the string is less than 1, return True.
4. If the last letter is equal to the first letter, recursively call the function with the argument as the sliced list with the first character and last character removed else return False.
5. Use an if statement if check if the returned value is True of False and print the final result.
6. Exit.
"""
def palindrome(string):
    if len(string) < 1:
        return True
    else:
        if string[-0] == string[-1]:
            return palindrome(string[1 : -1])
        else:
            return False
string = input("Enter a string: ")
if palindrome(string) == True:
    print ("String is a Palindrome!")
else:
    print ("String is not a Palindrome!")
