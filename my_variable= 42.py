# my_variable= 42
# print("initial value:", my_variable)

# my_variable=23
# print("changed value 1:", my_variable)

# my_variable="hrss"
# print("changed value 2:", my_variable)


# age= int(input("Enter your age:"))
# print("your age is:",age,"years")

# #WAP to find addition
# number1= int(input("Enter the number:"))
# number2= int(input("Enter the number"))
# number3= number1 + number2
# print("addition of two numbers is:",number3)

# #WAp to calculate simple interest
# def simple_interest(p,t,r):
#     print("The Principle is:", p)
#     print("The Time period is:", t)
#     print("The rate interest is:", r)

#     si= (p*t*r)/100

#     print("The simple interest is:", si)
    

# P= int(input("Enter a principle:"))
# T= int(input("Enter a time"))
# R= int(input("Enter a rate"))
# simple_interest(P,T,R)


# #take integer as input and tell positive or negative
# a= int(input("Enter the number:"))
# if(a>0):
#     print("Number is positive")
# elif(a<0):
#     print("Number is negative")
# else:
#     print("Number is equal 0")

# #take a positive integer as input and tell even or odd
# a= int(input("Enter a number:"))
# if(a%2==0):
#     print("Number is even")
# else:
#     print("Number is odd")

# #profit or loss and how much it
# cp= int(input("Enter cost price"))
# sp= int(input("Enter selling price"))
# if(cp>sp):
#     print("The loss occured of",cp-sp)
# elif(sp>cp):
#     print("The profit occured of", sp-cp)
# else:
#     print("no profit loss")

# #take positive integer and tell if 4 digit or not
# a= int(input("Enter a interger"))
# if(a<=9999 and a>=1000):
#     print("integer is 4 digit")
# else:
#     print("integer is not 4 digit")

# #take integer and tell if divisibe of 5 and 3
# a=int(input("Enter a integer"))
# if(a%5==0 and a%3==0):
#     print("Integer is divisible by 5 and 3")
# else:
#     print("Integer is not divisible by 5 and 3")

# #take integer and tell if divisible by 5 or 3
# a=int(input("Enter a number"))
# if(a%5==0 or a%3==0):
#     print("Integer is divisible by 5 or 3")
# else:
#     print("integer is not divisible by 5 or 3")

# #take 3 positive integer input and print greatest
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a integer"))
# if(a>b and a>c):
#     print("greatest number is:",a)
# elif(b>a and b> c):
#     print("greatest number is ", b)
# elif(c>a and c> b):
#     print("greatest number is ", c)
# else:
#     print("not any number is greatest")


# #year is leap or no
# a=int(input("Please enter a year"))
# if(a%4==0):
#     print("year is leap year")
# else:
#     print("year is not leap year")

# #take integer and tell if divisible by 3 or 5 but not 15
# a=int(input("enter a number"))
# if(a%3==0 or a%5==0):
#     if(a%15 != 0):
#         print("number is divisible by 3 or 5 but not 15")
#     else:
#         print("number is divisible by 3 or 5 and also 15")
# else:
#     print("number is not divisble by 3 or 5")

# #take percent from student and print grade
# a= int(input("enter a percentage"))
# if(a>=81 and a<=100):
#     print("Very g")
# elif(a>=61 and a<=80):
#     print("g")
# elif(a>41 and a<=60):
#     print("av")
# else:
#     print("fail")

# #print hello n times as input
# n=int(input("enter a number n "))

# print()
# for _ in range(n):
#     print("hello world")

# #print number 1 to 100
# for n in range(1, 101):
#     print(n)

# #print even 1 to 100
# for n in range (1,101):
#     if(n%2==0):
#         print(n)

# #disply  1,3,5,7,,9 till n
# n=int(input("enter number"))
# for i in range(1,n):
#     if (n%2 != 0):
#         print(i)

# #continue will skip even number
# for num in range(1,11):
#     if num%2 == 0:
#         continue
#     print(num)

# #1 to 10
# j=0
# while j<=10:
#     print(j)
#     j=j+1

# #1 to 10 even
# j=0
# while j<=10:
#     if(j%2==0):
#         print(j)
#     j=j+1

# #print 5* in row when row=n
# n=int(input("Enter number"))
# for i in range(n):
#     print("*" * 5)

# #pattr
# a=int(input("enter a number"))

# for i in range(1, a+1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()

# #list
# this_list= list(("apple","banana","cherry"))
# print(len(this_list))

# this_list.append("temha")
# print(this_list)

# this_list.insert(1,"orh")
# print(this_list)

mylist=("mango","pinapple","papaya")
# this_list.extend(mylist)
# print(this_list)

# this_list.remove("banana")
# print(this_list)

# this_list.pop(4)
# print(this_list)

print(mylist)
mylist.reverse()
print(mylist)

