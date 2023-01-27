# medium (very low success rate), heap
# https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem
# my solution works for about half of the test cases, but times out if len(A) > ~10000.
# note - should add ~"heap implementation in python" to stats.json when complete

class Heap:
    def __init__(self, input=[]):
        self.heap = input
        self.size = len(self.heap)
        self.__buildHeap(self.heap)

    def __buildHeap(self, array):
        # call sift down on every parent node, starting at the last one
        # parent nodes are first half of array rounded down
        for i in range(len(array) // 2, -1, -1):
            self.__siftDown(i)
        return array

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __siftDown(self, i):
        # compare to children nodes and swap with smallest
        child1 = 2 * i + 1 if len(self.heap) > 2*i+1 else -1
        child2 = 2 * i + 2 if len(self.heap) > 2*i+2 else -1
        smallest = i
        if child1 > 0 and self.heap[child1] < self.heap[smallest]:
            smallest = child1
        if child2 > 0 and self.heap[child2] < self.heap[smallest]:
            smallest = child2

        if smallest != i:
            self.__swap(i, smallest)
            self.__siftDown(smallest)

    def __siftUp(self, i):
        # continuously swap item with its parent until its position is valid
        if i != 0:
            parentIdx = (i - 1) // 2
            if self.heap[i] < self.heap[parentIdx]:
                self.__swap(i, parentIdx)
                self.__siftUp(parentIdx)

    def insert(self, x):
        self.size += 1
        self.heap.append(x)
        self.__siftUp(len(self.heap)-1)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.size -= 1
        self.__swap(0, len(self.heap) - 1)
        value = self.heap.pop()
        self.__siftDown(0)
        return value


def cookies(k, A):
    heap = Heap(sorted(A))
    iterations = 0
    while heap.size > 1 and heap.peek() < k:
        iterations += 1
        new_cookie = heap.remove() + heap.remove() * 2
        heap.insert(new_cookie)

    if heap.peek() >= k:
        return iterations
    else:
        return -1


# expected output: -1, 2, 7, 5
if __name__ == "__main__":
    print(cookies(10, [1, 1, 1]))  # -1
    print(cookies(7, [1, 2, 3, 9, 10, 12]))  # 2
    print(cookies(3581, [6214, 8543, 9266, 1150, 7498, 7209, 9398, 1529, 1032, 7384, 6784, 34, 1449, 7598, 8795, 756, 7803, 4112, 298, 4967, 1261, 1724, 4272, 1100, 9373]))  # 7
    print(cookies(90, [13, 47, 74, 12, 89, 74, 18, 38]))  # 5
