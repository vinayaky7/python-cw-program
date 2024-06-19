def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
number = 12
result = check_odd_even(number)
print(f"The number {number} is {result}")

number = 7
result = check_odd_even(number)
print(f"The number {number} is {result}")
