def factorial_iterative(n):
    factorial = 1
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Example usage:
try:
    num = int(input("Enter a number to find its factorial: "))
    print(f"The factorial of {num} is: {factorial_iterative(num)}")
except ValueError:
    print("Please enter a valid integer.")

