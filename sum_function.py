

#writing a function for calculating sum from 1 to n
def sumOneToN(n):
    sum = 0
    for i in range (1,n+1):
        sum +=i
    return sum

n = int(input("Enter n: "))
#call function
output = sumOneToN(n)
print("sum of all numbers:", output) 


n = int(input("Enter n: "))
output1 = sumOneToN(n)
print("sum of all numbers:", output1) 
