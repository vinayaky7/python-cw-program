def decimal_to_binary(n):
    if n == 0:
        return ''
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

# Example usage:
try:
    decimal_number = int(input("Enter a decimal number: "))

    if decimal_number >= 0:
        binary_representation = decimal_to_binary(decimal_number)
        print(f"The binary representation of {decimal_number} is: {binary_representation}")
    else:
        print("Please enter a non-negative integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
