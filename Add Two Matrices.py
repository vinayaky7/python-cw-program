def add_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices should have the same dimensions for addition."

    # Initialize a result matrix with zeros
    result = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]

    # Perform element-wise addition
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

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

    # Perform matrix addition
    if rows1 == rows2 and cols1 == cols2:
        result = add_matrices(matrix1, matrix2)
        print("\nMatrix Addition Result:")
        for row in result:
            print(row)
    else:
        print("\nMatrices must have the same dimensions for addition.")
except ValueError:
    print("Invalid input. Please enter integers for matrix elements.")
