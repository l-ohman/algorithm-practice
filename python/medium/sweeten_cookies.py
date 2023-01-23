# medium (very low success rate), heap
# https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem
# my solution works for about half of the test cases, but times out if len(A) > ~10000.
# would need to implement a heap to pass those test cases.

def mergeCookies(least_sweet, next_least_sweet):
    return least_sweet + next_least_sweet * 2


def cookies(k, A):
    A = sorted(A)
    iterations = 0

    while len(A) > 1 and A[0] < k:
        iterations += 1
        new_cookie = mergeCookies(A[0], A[1])
        A = A[2:]

        cookie_inserted = False
        for i in range(len(A)):
            if new_cookie <= A[i]:
                A.insert(i, new_cookie)
                cookie_inserted = True
                break
        if not cookie_inserted:
            A.append(new_cookie)

    if A[0] >= k:
        return iterations
    else:
        return -1


if __name__ == "__main__":
    print(cookies(10, [1, 1, 1]))  # -1
    print(cookies(7, [1, 2, 3, 9, 10, 12]))  # 2
    print(cookies(90, [13, 47, 74, 12, 89, 74, 18, 38]))  # 5
