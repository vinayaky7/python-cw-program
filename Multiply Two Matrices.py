def multiply_matrices(matrix1, matrix2):
    # Check dimensions for matrix multiplication
    if len(matrix1[0]) != len(matrix2):
        return "Cannot multiply matrices with these dimensions."

    # Dimensions of matrices
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    # Initialize result matrix with zeros
    result = [[0] * cols2 for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


# Example usage:
try:
    # Input matrix1
    rows1 = int(input("Enter the number of rows of matrix 1: "))
    cols1 = int(input("Enter the number of columns of matrix 1: "))
    matrix1 = []
    print("Enter the elements of matrix 1:")
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(int(input(f"Enter element [{i + 1}][{j + 1}]: ")))
        matrix1.append(row)

    # Input matrix2
    rows2 = int(input("Enter the number of rows of matrix 2: "))
    cols2 = int(input("Enter the number of columns of matrix 2: "))
    matrix2 = []
    print("Enter the elements of matrix 2:")
    for i in range(rows2):
        row = []
        for j in range(cols2):
            row.append(int(input(f"Enter element [{i + 1}][{j + 1}]: ")))
        matrix2.append(row)

    # Display matrices
    print("\nMatrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    # Perform matrix multiplication
    if cols1 == rows2:
        result = multiply_matrices(matrix1, matrix2)
        print("\nMatrix Multiplication Result:")
        for row in result:
            print(row)
    else:
        print("\nCannot multiply matrices with these dimensions.")
except ValueError:
    print("Invalid input. Please enter integers for matrix elements.")
