def transpose_matrix(matrix):
    # Get dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0])  # Assuming all rows have the same number of columns

    # Initialize a new matrix for the transpose
    transpose = [[0] * rows for _ in range(cols)]

    # Perform matrix transposition
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose


# Example usage:
try:
    # Input matrix
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i + 1}][{j + 1}]: ")))
        matrix.append(row)

    # Display original matrix
    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)

    # Perform matrix transposition
    transpose = transpose_matrix(matrix)

    # Display transposed matrix
    print("\nTransposed Matrix:")
    for row in transpose:
        print(row)
except ValueError:
    print("Invalid input. Please enter integers for matrix elements.")

