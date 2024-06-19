from enum import Enum

# Define an enumeration class
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Accessing enum members
print(Color.RED)        # Output: Color.RED
print(Color.RED.value)  # Output: 1

# Iterating over enum members
for color in Color:
    print(f"{color.name}: {color.value}")

# Checking membership correctly
if hasattr(Color, 'YELLOW'):
    print(Color.YELLOW in Color)
else:
    print('YELLOW is not represented in Color enum')
