# medium (very low success rate), heap
# https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem
# it seems i am unable to create an efficient heap, so i am using python heapq instead
import heapq

def cookies_original(k, A):
    heapq.heapify(A)
    iterations = 0

    while len(A) > 1 and A[0] < k:
        iterations += 1
        merged_cookie = heapq.heappop(A) + heapq.heappop(A) * 2
        heapq.heappush(A, merged_cookie)

    if A[0] >= k:
        return iterations
    else:
        return -1

# cleaned up solution
def cookies(k, A):
    heapq.heapify(A)
    iterations = 0

    while True:
        if A[0] >= k:
            return iterations
        elif len(A) < 2:
            return -1

        merged_cookie = heapq.heappop(A) + heapq.heappop(A) * 2
        heapq.heappush(A, merged_cookie)
        iterations += 1


# expected output: -1, 2, 7, 5, 999998
if __name__ == "__main__":
    print(cookies(10, [1, 1, 1]))  # -1
    print(cookies(7, [1, 2, 3, 9, 10, 12]))  # 2
    print(cookies(3581, [6214, 8543, 9266, 1150, 7498, 7209, 9398, 1529, 1032, 7384, 6784,
          34, 1449, 7598, 8795, 756, 7803, 4112, 298, 4967, 1261, 1724, 4272, 1100, 9373]))  # 7
    print(cookies(90, [13, 47, 74, 12, 89, 74, 18, 38]))  # 5
    print(cookies(1000000000, [1] * 1000000))  # 999998
