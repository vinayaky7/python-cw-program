def divide_numbers(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        divide_numbers(10, 0)  # ZeroDivisionError: division by zero
        divide_numbers(10, '2')  # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        divide_numbers(10, 2)  # No exception (normal case)
    except Exception as e:
        print(f"Error caught outside function: {e}")
