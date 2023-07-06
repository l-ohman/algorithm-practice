def transposeMatrix(matrix):
    height = len(matrix)
    width = len(matrix[0])
    output = [[0]*height for _ in range(width)]
    for i in range(height):
        for j in range(width):
            output[j][i] = matrix[i][j]
    return output

def transposeMatrix2(matrix):
    return list(zip(*matrix))
