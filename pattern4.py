"""
for n=4
A
AB
ABC
ABCD

row= n
column= equal to row number i
what to print=
"""

n = int(input("Enter n: "))
for i in range(65, 65+n):  # loop for rows
    for j in range(65, i+1):   # loop for columns
        print(chr(j), end="")
    print()
