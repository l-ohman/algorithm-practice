# matrix | medium
from copy import deepcopy

def rotate(matrix):
    matrix_copy = deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix_copy[len(matrix) - 1 - j][i]
    return matrix
    
if __name__ == "__main__":
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    # [7, 4, 1], [8, 5, 2], [9, 6, 3]