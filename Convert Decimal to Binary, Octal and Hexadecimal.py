def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")


def decimal_to_octal(decimal):
    return oct(decimal).replace("0o", "")


def decimal_to_hexadecimal(decimal):
    return hex(decimal).replace("0x", "")


# Example usage:
try:
    decimal_number = int(input("Enter a decimal number: "))

    binary_number = decimal_to_binary(decimal_number)
    octal_number = decimal_to_octal(decimal_number)
    hexadecimal_number = decimal_to_hexadecimal(decimal_number)

    print(f"The binary representation of {decimal_number} is: {binary_number}")
    print(f"The octal representation of {decimal_number} is: {octal_number}")
    print(f"The hexadecimal representation of {decimal_number} is: {hexadecimal_number}")
except ValueError:
    print("Please enter a valid decimal number.")
