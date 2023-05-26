# https://leetcode.com/problems/maximum-length-of-pair-chain/


def findLongestChain(pairs):
    pairs = sorted(pairs, key=lambda x: x[1])
    current, longest = pairs[0][1], 1
    for pair in pairs:
        if current < pair[0]:
            current = pair[1]
            longest += 1
    return longest


print(findLongestChain([[1,2],[7,8],[4,5]])) # 3
print(findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]])) # 3
print(findLongestChain([[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]])) # 4
