# https://leetcode.com/problems/reverse-words-in-a-string

# First solution (probably 10x better in practice)
def reverseWords(s):
    return " ".join(s.split()[::-1])

# Solution without using built-in methods
def reverseWords(s):
    words = []
    current = ""
    for char in s:
        if char != " ":
            current += char
        elif current != "":
            words.append(current)
            current = ""
    if current != "":
        words.append(current)
    output = ""
    print(words)
    for i in range(len(words)-1, -1, -1):
        output += words[i]
        if i != 0:
            output += " "
    return output
