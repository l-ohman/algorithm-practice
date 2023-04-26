# easy, string

def commonCharacters(strings):
    char_list = []

    for char in strings[0]:
        if char in char_list:
            continue
        valid_char = True
        for string in strings[1:]:
            if string.find(char) < 0:
                valid_char = False
                break
        if valid_char:
            char_list.append(char)

    return char_list


def commonCharactersSet(strings):
    common_chars = set(strings[0])
    for string in strings[1:]:
        common = set()
        for char in set(string):
            if char in common_chars:
                common.add(char)
        common_chars = common
    return list(common_chars)
