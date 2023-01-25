# easy, debugging
# https://www.hackerrank.com/challenges/one-week-preparation-kit-zig-zag-sequence/problem
# given incorrect solution, update a maximum of 3 lines to make it work
# note: not allowed to add or remove lines of code

def findZigZagSequence(a, n):
    a.sort()
    mid = n // 2 # calculation to get idx
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 # 2nd to least ele instead of last ele
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # "+" to "-"

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return