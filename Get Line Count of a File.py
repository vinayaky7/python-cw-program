#######################################Method 1: Using enumerate() with a Loop##################################
def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for _ in file)
    return line_count

# Example usage:
if __name__ == "__main__":
    filename = 'example.txt'  # Replace with your file path
    lines = count_lines(filename)
    print(f"Number of lines in '{filename}': {lines}")


# ####################################Method 2: Using len() with readlines()####################################
# def count_lines_readlines(filename):
#     with open(filename, 'r') as file:
#         lines = file.readlines()
#     return len(lines)
#
# # Example usage:
# if __name__ == "__main__":
#     filename = 'example.txt'  # Replace with your file path
#     lines = count_lines_readlines(filename)
#     print(f"Number of lines in '{filename}': {lines}")
