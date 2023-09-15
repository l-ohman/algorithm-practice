# https://leetcode.com/problems/path-with-maximum-probability/
# top 7% time, top 40% memory

import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # initialize graph from edges
        graph = collections.defaultdict(dict)
        for i in range(len(edges)):
            if succProb[i] == 0:
                continue
            n1, n2 = edges[i][0], edges[i][1]
            graph[n1][n2] = succProb[i]
            graph[n2][n1] = succProb[i]

        # breadth first search
        heap = [[0, start_node]]
        heapq.heapify(heap)
        visited = set()
        scores = {}
        while heap and end_node not in visited:
            p_alive, node = heapq.heappop(heap)
            if node not in graph or node in visited:
                continue
            visited.add(node)

            # process neighbors
            for neighbor, prob in graph[node].items():
                if neighbor in visited:
                    continue
                p_new = (1 - p_alive) * prob
                heapq.heappush(heap, [(1 - p_new), neighbor])

            prev = scores.get(node, 1)
            scores[node] = min(prev, p_alive)

        return 1 - scores.get(end_node, 1)
