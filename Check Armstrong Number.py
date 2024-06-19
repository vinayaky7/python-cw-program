def is_armstrong(number):
    # Convert number to string to count digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate sum of each digit raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return armstrong_sum == number


# Example usage:
try:
    num = int(input("Enter a number to check if it's an Armstrong number: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")
except ValueError:
    print("Please enter a valid integer.")
