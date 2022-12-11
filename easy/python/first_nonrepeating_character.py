# string / easy
# input: string of lowercase letters
# output: index of the first character that only appears once

# O(n) time | O(1) space
def first_nonrepeating_character(string):
    char_counts = {}
    for char in string:
        # 'get' method returns the value from the dict if it exists, or the value specified
        char_counts[char] = char_counts.get(char, 0) + 1

    for i in range(len(string)):
        if char_counts[string[i]] == 1:
            return i

    return -1
