# https://leetcode.com/problems/zigzag-conversion/description/


# first attempt - was able to pass many tests, but failed on most edge cases
def convert(s, numRows):
    interval = numRows + numRows // 2 if numRows >= 3 else numRows
    res = ""
    for i in range(numRows):
        curr = i
        if i == 0 or i == numRows - 1:
            while curr < len(s) and len(res) < len(s):
                res += s[curr]
                curr += interval
        else:
            while curr < len(s):
                offset = interval - i * 2
                res += s[curr]
                curr += offset
                if curr >= len(s):
                    break
                res += s[curr]
                curr += interval - offset
    return res


# second attempt - after researching an visual that shows the pattern
# (this is a reminder to use pen and paper when solving these problems!)
# pattern example for numRows=3: 1 2 3 2 1 2 3 2 1 2 3 2 1
# pattern example for numRows=4: 1 2 3 4 3 2 1 2 3 4 3 2 1 2
# beats 94% time and 92% space
def convert(s, numRows):
    rows = [""] * numRows
    going_up = True
    row = 0
    for i in range(len(s)):
        rows[row] += s[i]
        if numRows == 1:
            continue
        if row == 0:
            going_up = True
        elif row == numRows - 1:
            going_up = False
        row += 1 if going_up else -1
    return "".join(rows)
