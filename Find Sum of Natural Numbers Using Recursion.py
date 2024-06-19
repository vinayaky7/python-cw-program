def sum_of_natural_numbers(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)

# Example usage:
try:
    num = int(input("Enter a positive integer: "))

    if num > 0:
        result = sum_of_natural_numbers(num)
        print(f"The sum of natural numbers up to {num} is: {result}")
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
