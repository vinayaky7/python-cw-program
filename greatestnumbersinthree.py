#Take a 3 positive integers input and print the gratest of them

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

# #using logical operators
# #if n1 is greatest
# if n1 > n2 and n1 > n3:
#     print("n1 is greatest")
# #if n2 is greatest
# elif n2 > n1 and n2 > n3:
#     print("n2 is greatest")
# #if n3 is greatest
# else:
#     print("n3 is greatest")

#using nested if else statement
#comparing n1 and n2
if n1 > n2:
    #either n1 or n3 is greatest
    if n1>n3:
        print(n1, "is greatest element")
    else:
        print(n3, "is greatest element")
else:
    #either n2 or n3 is greatest
    if n2>n3:
        print(n2, "is greatest element")
    else:
        print(n3, "is greatest element")

