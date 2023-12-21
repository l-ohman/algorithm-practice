# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/


def kthSmallest(matrix, k):
    import heapq

    heap = []
    # using a max heap
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if len(heap) < k:
                heapq.heappush(heap, -matrix[i][j])
            elif -matrix[i][j] > heap[0]:
                heapq.heappushpop(heap, -matrix[i][j])
    return -heap[0]
