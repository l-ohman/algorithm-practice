# https://leetcode.com/problems/ransom-note

def canConstruct(ransomNote: str, magazine: str) -> bool:
    for letter in set(ransomNote):
        if ransomNote.count(letter) > magazine.count(letter):
            return False
    return True
