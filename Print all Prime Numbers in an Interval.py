def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage:
try:
    start = int(input("Enter the start of the interval: "))
    end = int(input("Enter the end of the interval: "))

    if start >= end:
        print("End of interval must be greater than start.")
    else:
        primes = print_primes_in_interval(start, end)
        if primes:
            print(f"Prime numbers between {start} and {end} are: {primes}")
        else:
            print(f"No prime numbers found between {start} and {end}")
except ValueError:
    print("Please enter valid integers for start and end of the interval.")
