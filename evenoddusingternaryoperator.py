#WAP to check if number is odd or even using ternary operator
num = int(input("Enter a number: "))

# output = "Even" if num / 2 == 0 else "odd"
# print("Output is", output)

print("Output is", "Even" if num % 2 == 0 else "odd")
