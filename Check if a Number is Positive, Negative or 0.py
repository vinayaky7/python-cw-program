def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage:
number = 5
result = check_number(number)
print(f"The number {number} is {result}")

number = -2.5
result = check_number(number)
print(f"The number {number} is {result}")

number = 0
result = check_number(number)
print(f"The number {number} is {result}")
