"""
5: Print the given pattern


            1
        1   2   3
    1   2   3   4   5
1   2   3   4   5   6   7

we need to print spaces= n-i columns
rows= n
columns= 2*i-1
what to print= column number
"""

n = int(input("Enter n: "))


for i in range(1, n+1):  # loop for rows
    # printing spaces
    print(" " * (n-i), end="")  # print spaces n-1 times
    # printing digits
    for j in range(1, 2 * i-1+1):
        print(j, end="")
    print()
