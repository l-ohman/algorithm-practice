# https://leetcode.com/problems/longest-substring-without-repeating-characters

def lengthOfLongestSubstring(s):
    hashmap = {}
    longest = 0
    j = 0

    for i in range(len(s)):
        if s[i] not in hashmap:
            longest = max(longest, i-j+1)
        else:
            last_seen = hashmap[s[i]]
            if last_seen < j:
                longest = max(longest, i-j+1)
            else:
                j = last_seen + 1
        hashmap[s[i]] = i

    return longest


print(lengthOfLongestSubstring("abcabcbb") == 3)  # "abc"
print(lengthOfLongestSubstring("bbbbb") == 1)  # "b"
print(lengthOfLongestSubstring("pwwkew") == 3)  # "wke"
