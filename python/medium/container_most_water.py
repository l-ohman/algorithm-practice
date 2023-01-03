# medium / array
# https://leetcode.com/problems/container-with-most-water/

def max_area(height):
	i, j = 0, len(height) - 1
	largest_area = 0

	while (j > i):
		current = min(height[i], height[j]) * (j - i)
		largest_area = max(current, largest_area)

		if height[i] < height[j]:
			i += 1
		else:
			j -= 1

	return largest_area

if __name__ == "__main__":
	print(max_area([1,8,6,2,5,4,8,3,7])) # 49
	print(max_area([1,1])) # 1
	print(max_area([1,8,100,2,100,4,8,3,7])) # 200
