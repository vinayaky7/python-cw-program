import math


def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Check the value of the discriminant
    if discriminant > 0:
        # Two real roots
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2 * a)
        x2 = (-b - sqrt_discriminant) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        # One real root (repeated root)
        x = -b / (2 * a)
        return x, x
    else:
        # Two complex roots (discriminant < 0)
        sqrt_discriminant = math.sqrt(abs(discriminant))
        real_part = -b / (2 * a)
        imag_part = sqrt_discriminant / (2 * a)
        x1 = complex(real_part, imag_part)
        x2 = complex(real_part, -imag_part)
        return x1, x2


# Example usage:
a = 1
b = -3
c = 2

x1, x2 = solve_quadratic(a, b, c)

print(f"The solutions are: x1 = {x1}, x2 = {x2}")

