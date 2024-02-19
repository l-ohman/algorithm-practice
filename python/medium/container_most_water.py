# medium / array
# https://leetcode.com/problems/container-with-most-water/


# 01/03/23
def max_area(height):
    i, j = 0, len(height) - 1
    largest_area = 0

    while j > i:
        current = min(height[i], height[j]) * (j - i)
        largest_area = max(current, largest_area)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return largest_area


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(max_area([1, 1]))  # 1
    print(max_area([1, 8, 100, 2, 100, 4, 8, 3, 7]))  # 200


# 02-19-24 (beats 83% time, 57% space)
# kinda crazy how my new solution looks exactly like the old one, despite not referencing it...
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        largest = 0
        while i < j:
            water = min(height[i], height[j]) * (j - i)
            largest = max(largest, water)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return largest
