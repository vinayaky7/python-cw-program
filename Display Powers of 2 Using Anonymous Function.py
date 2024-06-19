# Using lambda function with map
num_terms = 10  # Number of terms to display
powers_of_2 = map(lambda x: 2 ** x, range(num_terms))

# Print the powers of 2
print("Powers of 2 using lambda function:")
for power in powers_of_2:
    print(power)
