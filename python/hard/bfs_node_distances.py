# hard, BFS/graph
# https://www.hackerrank.com/challenges/bfsshortreach/problem
# currently only passing 50% of test cases (4/8)

def bfs(n, m, edges, s):
    graph = {}
    for i in range(n):
        graph[i+1] = []
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    distance_queue = [[s, 0]]
    nodes_visited = {}
    distances = [-1] * n
    
    while distance_queue:
        node, dist = distance_queue.pop()
        if node not in nodes_visited:
            nodes_visited[node] = 1
            distances[node-1] = dist
            for neighbor_node in graph[node]:
                distance_queue.append([neighbor_node, dist+6])
    
    return distances[:s-1] + distances[s:]
