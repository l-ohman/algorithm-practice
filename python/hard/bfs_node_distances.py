# hard, BFS/graph
# https://www.hackerrank.com/challenges/bfsshortreach/problem

# solution on 01-26-23
from collections import deque

def bfs(n, m, edges, s):
    graph = {}
    for i in range(n):
        graph[i+1] = set()
    for n1, n2 in edges:
        graph[n1].add(n2)
        graph[n2].add(n1)
    
    distance_queue = deque([(s, 0)])
    nodes_visited = {}
    distances = [-1] * n
    
    while distance_queue:
        node, dist = distance_queue.popleft()
        if node not in nodes_visited:
            nodes_visited[node] = 1
            distances[node-1] = dist
            for neighbor_node in graph[node]:
                distance_queue.append([neighbor_node, dist+6])
    
    return distances[:s-1] + distances[s:]


# solution on 07-10-23 (did not realize i had already done this problem)
def bfs(n, m, edges, s):
    # create graph (each index contains a nodes neighbors)
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a-1].append(b)
        graph[b-1].append(a)
    # record distances
    distances = [-1] * n
    distances[s-1] = 0
    # use queue to traverse graph with BFS
    queue = [s]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node-1]:
            if distances[neighbor-1] == -1:
                distances[neighbor-1] = distances[node-1] + 6
                queue.append(neighbor)
    return distances[:s-1] + distances[s:]
