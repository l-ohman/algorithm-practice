# string / easy
# inputs: str "c" of available characters, document to create with "c"
# output: boolean representing whether document can be created with characters in "c"

# O(n + m) time
def generate_document(characters, document):
    character_map = {}
    for i in range(len(characters)):
        if characters[i] in character_map:
            character_map[characters[i]] += 1
        else:
            character_map[characters[i]] = 1

    for i in range(len(document)):
        if not document[i] in character_map or character_map[document[i]] == 0:
            return False
        else:
            character_map[document[i]] -= 1

    return True
