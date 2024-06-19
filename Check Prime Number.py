def is_prime(number):
    # Check if number is less than or equal to 1
    if number <= 1:
        return False

    # Check for factors from 2 to sqrt(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Example usage:
try:
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
except ValueError:
    print("Please enter a valid integer")
