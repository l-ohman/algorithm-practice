# easy, string

# O(n^2)
def semordnilap(words):
    semordnilap_list = []
    for i in range(len(words)-1):
        for j in range(i+1, len(words)):
            if (words[i] == words[j][::-1]):
                semordnilap_list.append([words[i], words[j]])
    return semordnilap_list


# O(n)
def semordnilap(words):
    pairs = []
    word_map = {}
    for word in words:
        reversed = word[::-1]
        if reversed in word_map:
            pairs.append([reversed, word])
        else:
            word_map[word] = 1
    return pairs
