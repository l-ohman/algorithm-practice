# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column


# First attempt - beats 79% time complexity and 98% space complexity
def onesMinusZeros(grid):
    rows, columns = [0] * len(grid), [0] * len(grid[0])

    # calculate rows
    for i in range(len(grid)):
        row = grid[i]
        for val in row:
            rows[i] += 1 if val == 1 else -1

    # calculate columns
    for j in range(len(grid[0])):
        column = []
        for i in range(len(grid)):
            column.append(grid[i][j])
        for val in column:
            columns[j] += 1 if val == 1 else -1

    # update values in grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = rows[i] + columns[j]
    return grid
