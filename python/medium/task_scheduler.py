# https://leetcode.com/problems/task-scheduler/?envType=daily-question&envId=2024-03-19


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # determinate is most frequent element
        count = Counter(tasks)
        most_freq = max(count.values())
        # also need number of elements that are equal to most freq
        num_most_freq = 0
        for c in count.values():
            if c == most_freq:
                num_most_freq += 1

        # either we need to wait for cooling or we do not
        wait = (most_freq - 1) * (n + 1) + num_most_freq
        return max(wait, len(tasks))
