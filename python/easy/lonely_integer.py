# easy, array
# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem

def lonelyinteger(a):
    a = sorted(a)
    for i in range(0, len(a), 2):
        if (i == len(a) - 1) or (a[i] != a[i+1]):
            return a[i]

# clever solution by @johannzen using set and sum (!)
# def lonelyinteger(a):
#    sum_of_set = sum(set(a))
#    sum_of_list = sum(a)
#    return sum_of_set*2-sum_of_list
