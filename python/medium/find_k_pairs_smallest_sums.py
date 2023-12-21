# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

import heapq


def kSmallestPairs(nums1, nums2, k):
    pairs = [(nums1[0] + nums2[0], 0, 0)]
    heapq.heapify(pairs)

    visited = set()
    res = []
    while len(pairs) > 0 and len(res) < k:
        (_, i, j) = heapq.heappop(pairs)
        if (i, j) not in visited:
            res.append([nums1[i], nums2[j]])
            visited.add((i, j))

        if j < len(nums2) - 1 and (i, j + 1) not in visited:
            heapq.heappush(pairs, (nums1[i] + nums2[j + 1], i, j + 1))
        if i < len(nums1) - 1 and (i + 1, j) not in visited:
            heapq.heappush(pairs, (nums1[i + 1] + nums2[j], i + 1, j))
    return res[:k]
