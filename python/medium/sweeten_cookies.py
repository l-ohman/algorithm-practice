# medium (very low success rate), heap
# https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem
# my solution works for about half of the test cases, but times out if len(A) > ~10000.
# would need to implement a heap to pass those test cases.

class Heap:
    def __init__(self, input=[]):
        self.heap = input
        self.size = len(self.heap)
        self.__build(self.heap)

    def __swapItems(self, i, j):
        itm = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = itm

    def heapify(self, i):
        # compare to children and swap with smallest
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left

        if smallest != i:
            print("swapping in heapify --", f'i: {i} val: {self.heap[i]} | i: {smallest} val: {self.heap[smallest]}')
            self.__swapItems(i, smallest)
            self.heapify(smallest)

    def insert(self, x):
        self.size += 1
        self.heap.append(x)
        def parent(i): return (i - 1) // 2

        i = len(self.heap) - 1
        j = parent(i)
        while (self.heap[i] < self.heap[j]):
            self.__swapItems(i, j)
            i = j
            j = parent(i)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.size -= 1
        min = self.heap[0]
        self.__swapItems(0, len(self.heap) - 1)
        self.heap = self.heap[:self.size]
        self.heapify(0)
        return min

    def __build(self, array):
        for i in range(len(array) // 2, -1, -1):
            self.heapify(array[i])
        return array


def mergeCookies(least_sweet, next_least_sweet):
    return least_sweet + next_least_sweet * 2


def cookies(k, A):
    heap = Heap(sorted(A))
    iterations = 0
    print("heap:", heap.heap)

    while heap.size > 1 and heap.peek() < k:
        print("\nadding new cookie...\n")
        iterations += 1
        new_cookie = mergeCookies(heap.remove(), heap.remove())
        heap.insert(new_cookie)
        print("heap:", heap.heap, "| newest cookie:", new_cookie)

    if heap.peek() >= k:
        return iterations
    else:
        return -1


if __name__ == "__main__":
    # print(cookies(10, [1, 1, 1]))  # -1
    # print(cookies(7, [1, 2, 3, 9, 10, 12]))  # 2
    # print(cookies(90, [13, 47, 74, 12, 89, 74, 18, 38]))  # 5
    print(cookies(3581, [6214, 8543, 9266, 1150, 7498, 7209, 9398, 1529, 1032, 7384, 6784,
          34, 1449, 7598, 8795, 756, 7803, 4112, 298, 4967, 1261, 1724, 4272, 1100, 9373]))  # 7
