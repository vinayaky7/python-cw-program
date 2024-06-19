def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
try:
    num = int(input("Enter a non-negative integer: "))

    if num >= 0:
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")
    else:
        print("Please enter a non-negative integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
