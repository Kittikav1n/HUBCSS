def add_matrices(a, b):
    # Assumes a and b are lists of lists (matrices) of the same size
    result = []
    for row_a, row_b in zip(a, b):
        result.append([x + y for x, y in zip(row_a, row_b)])
    return result

# Example usage
matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = [
    [5, 6],
    [7, 8]
]
sum_matrix = add_matrices(matrix1, matrix2)
print("Sum Matrix:", sum_matrix)