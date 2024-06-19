def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return fib_sequence
    else:
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Example usage:
try:
    num_terms = int(input("Enter the number of terms in Fibonacci sequence: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        fib_sequence = fibonacci_iterative(num_terms)
        print("Fibonacci sequence:", fib_sequence)
except ValueError:
    print("Please enter a valid integer.")
