# string / easy
# input: string of lowercase letters and integer "x"
# output: string where ever letter if shifted "x" indicies in the alphabet

# O(n) time | O(n) space
def caesar_cipher_encryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_map = {}
    for i in range(len(alphabet)):
        alphabet_map[i] = alphabet[i]
        alphabet_map[alphabet[i]] = i

    encrypted_string = ""
    for i in range(len(string)):
        shifted_index = (alphabet_map[string[i]] + key) % 26
        encrypted_string += alphabet_map[shifted_index]

    return encrypted_string
