def swap_variables(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a  # Simultaneous assignment to swap values
    print(f"After swapping: a = {a}, b = {b}")

# Example usage:
a = 5
b = 10

swap_variables(a, b)
