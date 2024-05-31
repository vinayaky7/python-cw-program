"""
for n=4
1
12
123
1234

row= n
column= equal to row number i
what to print= cloumn number j
"""


n = int(input("Enter n: "))
for i in range(1,n+1):  # loop for rows
    for j in range(1, i+1):   # loop for columns
        print(j, end="")
    print()


