# https://www.hackerrank.com/challenges/non-divisible-subset


def nonDivisibleSubset(k, s):
    mods = [n % k for n in s]
    count_map = {x: 0 for x in range(k)}
    for mod in mods:
        count_map[mod] += 1

    total = 0
    for mod, count in count_map.items():
        if mod == 0:
            total += min(count, 1)
        elif k % 2 == 0 and mod == k / 2:
            total += min(count, 1)
        else:
            if count > count_map[k - mod]:
                total += count
            elif count == count_map[k - mod]:
                total += count / 2
    return int(total)
