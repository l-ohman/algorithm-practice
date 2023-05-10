# https://leetcode.com/problems/add-binary/

def addBinary(a, b):
    val = 0
    for num in a, b:
        digit = 1
        for i in range(len(num)-1, -1, -1):
            val += int(num[i]) * digit
            digit *= 2
    return bin(val)[2:]
