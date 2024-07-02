def get_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Example usage:
if __name__ == "__main__":
    length = 5
    width = 3
    area, perimeter = get_rectangle_properties(length, width)
    print(f"Rectangle with length {length} and width {width}:")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

# #####################################Using NamedTuples:#####################################
# from collections import namedtuple
#
# def get_rectangle_properties(length, width):
#     Rectangle = namedtuple('Rectangle', ['area', 'perimeter'])
#     area = length * width
#     perimeter = 2 * (length + width)
#     return Rectangle(area, perimeter)
#
# # Example usage:
# if __name__ == "__main__":
#     length = 5
#     width = 3
#     rectangle = get_rectangle_properties(length, width)
#     print(f"Rectangle with length {length} and width {width}:")
#     print(f"Area: {rectangle.area}")
#     print(f"Perimeter: {rectangle.perimeter}")
