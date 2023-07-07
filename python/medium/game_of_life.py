# https://leetcode.com/problems/game-of-life

# RULES:
# Live=1, Dead=0
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# ASSIGNMENT:
# Given the current state of the m x n grid board, modify the input to reflect the next state.

from copy import deepcopy


def getNeighbors(board, x, y):
    width = len(board[0])
    height = len(board)
    neighbors = []
    if x > 0:
        neighbors.append(board[y][x-1])
        if y > 0:
            neighbors.append(board[y-1][x-1])
        if y < height - 1:
            neighbors.append(board[y+1][x-1])
    if x < width - 1:
        neighbors.append(board[y][x+1])
        if y > 0:
            neighbors.append(board[y-1][x+1])
        if y < height - 1:
            neighbors.append(board[y+1][x+1])
    if y > 0:
        neighbors.append(board[y-1][x])
    if y < height - 1:
        neighbors.append(board[y+1][x])
    return neighbors


def gameOfLife(board):
    board_copy = deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            neighbors = getNeighbors(board_copy, j, i)
            if board_copy[i][j] == 1:
                if neighbors.count(1) < 2 or neighbors.count(1) >= 4:
                    board[i][j] = 0
                else:
                    board[i][j] = 1
            else:
                if neighbors.count(1) == 3:
                    board[i][j] = 1

# Above solution is rather inefficient, but at least it's readable
# An improved solution could use something as below to check neighbors more easily:
directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
