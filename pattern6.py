"""
for n=4
a
ab
abc
abcd

row= n
column= equal to row number i
what to print=
"""

n = int(input("Enter n: "))
for i in range(97, 97+n):  # loop for rows
    for j in range(97, i+1):   # loop for columns
        print(chr(j), end="")
    print()
