# https://leetcode.com/problems/rotting-oranges/

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first get starting points (rotten oranges)
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((0, (i, j)))

        # keep track of visited nodes
        visited = set()
        largest = 0
        while queue:
            time, coord = queue.popleft()
            if coord in visited:
                continue
            visited.add(coord)

            if time > largest:
                largest = time

            n = self.getNeighbors(grid, coord[0], coord[1])
            for i, j, val in n:
                if (i, j) in visited or val != 1:
                    continue
                grid[i][j] = 2
                queue.append((time+1, (i, j)))

        # check if any fresh oranges remain, then return largest
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return largest

    def getNeighbors(self, grid, i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j, grid[i-1][j]))
        if j > 0:
            neighbors.append((i, j-1, grid[i][j-1]))
        if i < len(grid)-1:
            neighbors.append((i+1, j, grid[i+1][j]))
        if j < len(grid[0])-1:
            neighbors.append((i, j+1, grid[i][j+1]))
        return neighbors
