# https://leetcode.com/problems/min-cost-to-connect-all-points

# first solution, that uses util functions to compare/combine trees by storing their "roots" (parent nodes)
# top 40% runtime, top 30% memory
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # calculate all possible edges
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                edges.append((d, i, j))

        # keep track of the parent of every node (we do this to check if trees are connected)
        parents = [i for i in range(n)]
        # utility fn to get parent idx of a node

        def find(x):
            # to get root of a tree, we must find a node where the parent is itself
            if parents[x] == x:
                return x
            parents[x] = find(parents[x])
            return parents[x]
        # utility fn to merge 2 trees

        def combine(x, y):
            parents[find(x)] = find(y)

        min_cost = num_edges = 0
        # sort edges by distance and loop through
        edges.sort(key=lambda x: x[0])
        for dist, i, j in edges:
            # if 2 nodes don't have a common parent, unite them with this edge
            if find(i) != find(j):
                combine(i, j)
                min_cost += dist
                num_edges -= 1
            # we have a spanning tree when num_edges is (n - 1)
            if num_edges == n-1:
                break
        return min_cost
