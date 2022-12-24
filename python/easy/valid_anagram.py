# easy | hashmap / string

def is_valid_anagram(s: str, t: str):
    # rtype: bool
    char_map = {}
    for char in s:
        if char not in char_map:
            char_map[char] = 0
        char_map[char] += 1
    for char in t:
        if char not in char_map:
            return False
        char_map[char] -= 1
        if char_map[char] == 0:
            del char_map[char]

    return len(char_map) == 0
    

if __name__ == "__main__":
    print(is_valid_anagram('cat', 'dog'))          # False
    print(is_valid_anagram('racecar', 'car'))      # False
    print(is_valid_anagram('plumbob', 'bomplub'))  # True
