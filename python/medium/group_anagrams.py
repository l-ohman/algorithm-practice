# medium | hashmap / string
# https://leetcode.com/problems/group-anagrams/

def group_anagrams(strs):
    # key: hashmap-string, val: array of words
    hashmap_dict = {}
    
    for i in range(len(strs)):
        hashmap_key = ''.join(sorted(strs[i]))
        
        if hashmap_key in hashmap_dict:
            hashmap_dict[hashmap_key].append(strs[i])
        else:
            hashmap_dict[hashmap_key] = [strs[i]]
    
    output = []
    for key in hashmap_dict:
        output.append(hashmap_dict[key])
    return output

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    # [["bat"],["nat","tan"],["ate","eat","tea"]]
