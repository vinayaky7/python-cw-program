def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Example usage:
try:
    num_terms = int(input("Enter the number of terms in Fibonacci sequence: "))

    fib_sequence = fibonacci(num_terms)
    if isinstance(fib_sequence, str):
        print(fib_sequence)
    else:
        print(f"Fibonacci sequence of {num_terms} terms:")
        print(fib_sequence)
except ValueError:
    print("Please enter a valid integer.")
