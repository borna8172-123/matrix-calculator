matrix = []
matrix1 = []



for i in range(3):
    values = list(map(int, input("Enter the values of the matrix separated by spaces: ").split()))
    matrix.append(values)

for i in range(3):
    values2 = list(map(int, input("Enter the values of the matrix separated by spaces: ").split()))
    matrix1.append(values2)

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1,matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result
def multiply_matrices(A, B):

    result = []

    for i in range(len(A)):

        row = []

        for j in range(len(B[0])):

            total = 0

            for k in range(len(B)):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result

print(f"the results of multiplying the two matrices is {multiply_matrices(matrix, matrix1)}")
print(f"the results of adding the two matrices is {add_matrices(matrix, matrix1)}")
print(f"the results of subtracting the two matrices is {subtract_matrices(matrix, matrix1)}")
