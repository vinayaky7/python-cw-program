def count_digits(number):
    # Convert number to string and use len() to count digits
    num_str = str(number)
    return len(num_str)

# Example usage:
if __name__ == "__main__":
    number = 12345
    digit_count = count_digits(number)
    print(f"Number of digits in {number}: {digit_count}")
