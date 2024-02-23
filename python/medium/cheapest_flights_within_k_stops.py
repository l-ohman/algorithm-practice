# https://leetcode.com/problems/cheapest-flights-within-k-stops/?envType=daily-question&envId=2024-02-23


# friendly reminder to practice more graph problems like this
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = defaultdict(list)
        distances = [-1 for _ in range(n)]
        for start, end, cost in flights:
            graph[start].append([end, cost])

        distances[src] = stops = 0
        q = deque([src])
        while q and stops <= k:
            # creating a duplicate so we can modify while maintaining original
            d = list(distances)
            for _ in range(len(q)):
                curr = q.popleft()
                for end, cost in graph[curr]:
                    if d[end] == -1 or d[end] > d[curr] + cost:
                        d[end] = distances[curr] + cost
                        q.append(end)
            # update stopcount and distances
            stops += 1
            distances = d
        return distances[dst]
