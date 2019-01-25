"""
Problem Statement : Python program to copy the contents of one file into another
"""

"""
Problem Solution
1. Open one file called test.txt in read mode.
2. Open another file out.txt in write mode.
3. Read each line from the input file and write it into the output file.
4. Exit.
"""

with open(test.txt, 'r') as f:
    with open(out.txt, 'w') as f1:
        for line in f:
            f1.write(line)
