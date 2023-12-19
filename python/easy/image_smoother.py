# https://leetcode.com/problems/image-smoother/


# first attempt - beast 76% time and 24% memory
# (the code is a bit messy, but i'm satisfied enough with the approach)
def imageSmoother(img):
    copy = [[0] * len(img[0]) for row in img]
    for i in range(len(img)):
        for j in range(len(img[0])):
            total = img[i][j]
            count = 1
            if i > 0 and i <= len(img):
                total += img[i - 1][j]
                count += 1
                if j > 0 and j <= len(img[0]) - 1:
                    total += img[i - 1][j - 1]
                    count += 1
                if j < len(img[0]) - 1 and j >= 0:
                    total += img[i - 1][j + 1]
                    count += 1
            if i < len(img) - 1 and i >= 0:
                total += img[i + 1][j]
                count += 1
                if j > 0 and j <= len(img[0]) - 1:
                    total += img[i + 1][j - 1]
                    count += 1
                if j < len(img[0]) - 1 and j >= 0:
                    total += img[i + 1][j + 1]
                    count += 1
            if j > 0 and j <= len(img[0]) - 1:
                total += img[i][j - 1]
                count += 1
            if j < len(img[0]) - 1 and j >= 0:
                total += img[i][j + 1]
                count += 1
            average = total // count
            copy[i][j] = average
    return copy
