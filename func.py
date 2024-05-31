# #write a function that poimts hello world

# def printHello():
#     #body of function
#     print("Hello World")


# printHello()



#function which takes 2 numbers as input and returns their sum
def add(n1=5,n2=2):
    print("n1:",n1)
    print("n2",n2)
    sum = n1+n2
    return sum

#positional arguments
#print("The sum is:", add(3,2))

#keyword arguments (named argumets)
#print("The sum is:", add(n1=3,n2=2))
 
#default arguments
# print("The sum is:", add(5))    #n2 will tale default value

def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

# output = addAllNumbers(2,3,5) #arbitrary aguments values as many values required
# print("the op is : ", output)


def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

studentInfo(name="vin", age = 28, city = "Pune" )
studentInfo(name="urvi", age = 22, city = "Delhi" )