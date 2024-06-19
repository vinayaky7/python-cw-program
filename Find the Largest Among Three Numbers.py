def find_largest(a, b, c):
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    return largest

# Example usage:
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    largest = find_largest(num1, num2, num3)
    print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
except ValueError:
    print("Please enter valid numbers.")
