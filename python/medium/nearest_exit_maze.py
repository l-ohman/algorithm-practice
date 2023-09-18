# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/


from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(0, entrance)])
        while queue:
            dist, location = queue.popleft()
            x, y = location[1], location[0]
            if maze[y][x] == "+":
                continue

            # as soon as we arrive at exit, we want to return the distance
            if (x == 0 or x == len(maze[0])-1) or (y == 0 or y == len(maze)-1):
                # first check if we are on border of maze
                # then make sure this is not a wall or the entrance
                if maze[y][x] == "." and location != entrance:
                    return dist
            maze[y][x] = "+"

            # add valid moves to queue
            moves = self.validMoves(maze, x, y)
            for y, x in moves:
                if maze[y][x] == "+":
                    continue
                queue.append((dist+1, [y, x]))
        return -1

    # helper function for readability
    def validMoves(self, maze, x, y):
        moves = []
        if x > 0 and maze[y][x-1] == ".":
            moves.append([y, x-1])
        if x < len(maze[0])-1 and maze[y][x+1] == ".":
            moves.append([y, x+1])
        if y > 0 and maze[y-1][x] == ".":
            moves.append([y-1, x])
        if y < len(maze)-1 and maze[y+1][x] == ".":
            moves.append([y+1, x])
        return moves
