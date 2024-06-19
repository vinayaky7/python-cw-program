def sum_of_natural_numbers(n):
    if n <= 0:
        return "Please enter a positive integer."
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Example usage:
try:
    num = int(input("Enter a positive integer: "))
    result = sum_of_natural_numbers(num)
    print(f"The sum of natural numbers up to {num} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
