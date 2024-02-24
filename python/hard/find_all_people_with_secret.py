# https://leetcode.com/problems/find-all-people-with-secret/?envType=daily-question&envId=2024-02-24


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        times, meet_at_time = set(), []
        for p1, p2, t in meetings:
            if t not in times:
                meet_at_time.append([])
                times.add(t)
            meet_at_time[-1].append((p1, p2))

        knows = set([0, firstPerson])
        for g in meet_at_time:
            local_knows = set()
            # need to graph this mtg to see who shares to who
            graph = defaultdict(list)
            for p1, p2 in g:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in knows:
                    local_knows.add(p1)
                if p2 in knows:
                    local_knows.add(p2)

            # then use queue to update knowledge
            q = deque((local_knows))
            while q:
                p1 = q.popleft()
                knows.add(p1)
                for p2 in graph[p1]:
                    if p2 not in knows:
                        knows.add(p2)
                        q.append(p2)
        return list(knows)
