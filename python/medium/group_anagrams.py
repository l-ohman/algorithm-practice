# medium | hashmap / string
# https://leetcode.com/problems/group-anagrams/


# 12/25/22
def group_anagrams(strs):
    # key: hashmap-string, val: array of words
    hashmap_dict = {}

    for i in range(len(strs)):
        hashmap_key = "".join(sorted(strs[i]))

        if hashmap_key in hashmap_dict:
            hashmap_dict[hashmap_key].append(strs[i])
        else:
            hashmap_dict[hashmap_key] = [strs[i]]

    output = []
    for key in hashmap_dict:
        output.append(hashmap_dict[key])
    return output


# 02/06/24
# beats 95% time, 75% memory
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charmap = {}
        for word in strs:
            letters = "".join(sorted(list(word)))
            if letters not in charmap:
                charmap[letters] = []
            charmap[letters].append(word)
        return charmap.values()
