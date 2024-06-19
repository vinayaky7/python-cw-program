def find_numbers_divisible(start, end, divisor):
    if start > end:
        return "Start of range must be less than or equal to end of range."

    divisible_numbers = []
    for num in range(start, end + 1):
        if num % divisor == 0:
            divisible_numbers.append(num)

    return divisible_numbers


# Example usage:
try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    divisor = int(input("Enter the divisor: "))

    numbers = find_numbers_divisible(start, end, divisor)
    if isinstance(numbers, list):
        if numbers:
            print(f"Numbers divisible by {divisor} between {start} and {end} are: {numbers}")
        else:
            print(f"No numbers divisible by {divisor} found between {start} and {end}")
    else:
        print(numbers)
except ValueError:
    print("Please enter valid integers.")
