#take +ve integer and tell if it is four digit or not

number = int(input("Enter the number: "))

if number >= 1000 and number <= 9999:
    print("It is four digit number")
else:
    print("not a four digit number")

