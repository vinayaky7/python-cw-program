import random

def generate_random_float_range(low, high):
    random_number = random.uniform(low, high)
    return random_number

# Example usage:
low = 1.0
high = 10.0

random_float_range = generate_random_float_range(low, high)
print(f"Random float between {low} and {high}: {random_float_range}")
