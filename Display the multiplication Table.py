def multiplication_table(num):
    for i in range(1, 11):  # Generate numbers from 1 to 10
        print(f"{num} x {i} = {num * i}")

# Example usage:
try:
    num = int(input("Enter a number to display its multiplication table: "))
    multiplication_table(num)
except ValueError:
    print("Please enter a valid integer.")
