# Function to calculate the area of a triangle
def calculate_area(base, height):
    return 0.5 * base * height

# Input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area = calculate_area(base, height)

# Print the result
print(f"The area of the triangle is: {area}")
