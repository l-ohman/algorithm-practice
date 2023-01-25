# easy, hashmap
# 20 min

def countOnesBinary(num):
    binary_num = bin(num)
    ones_count = 0
    for i in range(len(binary_num)):
        if binary_num[i] == "1":
            ones_count += 1
    return ones_count


def rearrange(elements):
    elements_by_ones = {}

    for i in range(len(elements)):
        one_count = countOnesBinary(elements[i])
        if one_count not in elements_by_ones:
            elements_by_ones[one_count] = []
        elements_by_ones[one_count].append(elements[i])

    result = []
    sorted_keys = sorted(elements_by_ones.keys())
    for i in range(len(sorted_keys)):
        key = sorted_keys[i]
        result += sorted(elements_by_ones[key])
    return result
