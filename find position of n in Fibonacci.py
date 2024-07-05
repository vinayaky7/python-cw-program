'''Python Program for nth multiple of a number in Fibonacci Series

Given two integers n and k. Find position the nth multiple of K in the Fibonacci series. 
Examples:

Input: k = 2, n = 3
Output: 9, 3rd multiple of 2 in Fibonacci Series is 34 that appears at position 9.

Input: k = 4, n = 5 
Output: 30, 5th multiple of 4 in Fibonacci Series is 832040 which appears at position 30.'''

# Python Program to find position of n\'th multiple
# of a number k in Fibonacci Series

def findPosition(k, n):
    f1 = 0
    f2 = 1
    i =2; 
    while i!=0:
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;

        if f2%k == 0:
            return n*i

        i+=1
        
    return 


# Multiple no.
n = 5;
# Number of whose multiple we are finding
k = 4;

print("Position of n\'th multiple of k in"
                "Fibonacci Series is", findPosition(k,n));

# Code contributed by Mohit Gupta_OMG
