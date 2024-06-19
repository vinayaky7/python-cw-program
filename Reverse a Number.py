def reverse_number(number):
    # Convert number to string and reverse using slicing
    reversed_number = str(number)[::-1]

    # Convert reversed string back to integer
    reversed_number = int(reversed_number)

    return reversed_number


# Example usage:
if __name__ == "__main__":
    number = 12345
    reversed_num = reverse_number(number)
    print(f"Original number: {number}")
    print(f"Reversed number: {reversed_num}")
