# easy, hashmap
# 25 min

def countLetters(s):
    mapString = {}
    for i in range(len(s)):
        if s[i] not in mapString:
            mapString[s[i]] = 0
        mapString[s[i]] += 1
    return mapString


def compareStrings(a, b):
    if (len(a) != len(b)):
        return "NO"
    mapA = countLetters(a)
    mapB = countLetters(b)

    for letter in mapA:
        if letter not in mapB:
            mapB[letter] = 0
        mapB[letter] = abs(mapB[letter] - mapA[letter])
    for count in mapB.values():
        if count > 3:
            return "NO"
    return "YES"


def areAlmostEquivalent(s, t):
    result = []
    for i in range(len(s)):
        result.append(compareStrings(s[i], t[i]))
    return result
