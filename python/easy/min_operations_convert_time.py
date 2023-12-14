# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/


def convertTime(current, correct):
    current = int(current[:2]) * 60 + int(current[3:])
    correct = int(correct[:2]) * 60 + int(correct[3:])
    difference = correct - current

    count = 0
    for num in [60, 15, 5, 1]:
        count += difference // num
        difference %= num

    return count
