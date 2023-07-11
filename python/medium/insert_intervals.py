# https://leetcode.com/problems/insert-interval

# three main cases:
#   new interval is AFTER current interval
#   new interval is BEFORE current interval
#   new interval is IN current interval


def insert(intervals, newInterval):
    output = []
    for i in range(len(intervals)):
        if newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
        elif newInterval[1] < intervals[i][0]:
            output.append(newInterval)
            newInterval = intervals[i]
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
    output.append(newInterval)
    return output


intervals, newInterval = [[1, 3], [6, 9]], [2, 5]
print(insert(intervals, newInterval) == [[1, 5], [6, 9]])
intervals, newInterval = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
print(insert(intervals, newInterval) == [[1, 2], [3, 10], [12, 16]])
