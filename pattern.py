"""
print the given pattern
for n=1
*****
for n=2
*****
*****
for n=3
*****
*****
*****
important 3 things: rows 3, columns 5, what to print *
"""

n = int(input("Enter n: "))

for _ in range(n):
    print("*" * 5)      #it will print * 5 times

