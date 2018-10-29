"""
Problem Statement : Python Program to Take in the Marks of 5 Subjects and Display the Grade
"""
print "Problem Statement : Python Program to Take in the Marks of 5 Subjects and Display the Grade"
sub1 = int(raw_input("Enter the mark for subject1: "))
sub2 = int(raw_input("Enter the mark for subject2: "))
sub3 = int(raw_input("Enter the mark for subject3: "))
sub4 = int(raw_input("Enter the mark for subject4: "))
sub5 = int(raw_input("Enter the mark for subject5: "))

add_of_five_subjects = sub1 + sub2 + sub3 + sub4 + sub5
avg = add_of_five_subjects / 5


print "The Average of five subject:", avg

if avg >= 80 or avg > 100:
    print "Grade A"
elif avg >= 60:
    print "Grade B"
elif avg >= 50:
    print "Grade C"
elif avg >= 40:
    print "Grade D"
else:
    print "Grade E"
