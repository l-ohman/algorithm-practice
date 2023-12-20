# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


# first attempt, beats 95% time and 11% memory
def letterCombinations(digits):
    if len(digits) == 0:
        return []
    letter_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    combinations = [l for l in letter_map[digits[0]]]
    if len(digits) == 1:
        return combinations

    for digit in digits[1:]:
        letters = letter_map[digit]
        new_combs = []
        for letter in letters:
            for c in combinations:
                new_combs.append(c + letter)
        combinations = new_combs
    return combinations


print(
    sorted(letterCombinations("23"))
    == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
)
print(letterCombinations("") == [])
print(letterCombinations("2") == ["a", "b", "c"])
