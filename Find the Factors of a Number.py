import math

def find_factors(number):
    factors = []
    # Iterate through all numbers from 1 to the square root of number
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            # Add the corresponding factor n // i
            if i != number // i:
                factors.append(number // i)
    # Sort the factors list
    factors.sort()
    return factors

# Example usage:
try:
    num = int(input("Enter a number: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        factors = find_factors(num)
        print(f"The factors of {num} are: {factors}")
except ValueError:
    print("Please enter a valid integer.")
