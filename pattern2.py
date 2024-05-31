"""
print given pattern
for n=4
1234
1234
1234
1234

for n=6
123456
123456
123456
123456
123456
123456

rows=n
colums=n
what to print= 1 to n numbers
"""


n = int(input("Enter n: "))
# cloumn variable j, rows looping variable i
for i in range(n):
    for j in range(1,n+1):  # normally range indexing starting from 0 so we required to start indexing from 1, exact n times row so take n+1
        print(j, end="")    # end is used for cursor should not go to next line i e 12345
    print()

