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


# alternate version
# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem
# this version permits upper/lower case letters and non-alpha characters (such as "-")

# maps created with fn using enumerate and dict
letter_to_int = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
                 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
int_to_letter = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
                 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

def caesarCipher(s, k):
    encrypted_str = ""
    for i in range(len(s)):
        letter = s[i].lower()
        if letter not in letter_to_int:
            encrypted_str += s[i]
        else:
            shifted_idx = (letter_to_int[letter] + k) % 26
            letter = int_to_letter[shifted_idx]

            if s[i].isupper():
                letter = letter.upper()
            encrypted_str += letter
    return encrypted_str


# alternate solution without using prebuilt maps
# idea to merge shifted dicts with "|" from @tuo20482's solution
def caesarCipherThree(s, k):
    k = k % 26
    l_alpha = "abcdefghijklmnopqrstuvwxyz"
    u_alpha = l_alpha.upper()
    alpha_map = dict(zip(l_alpha, l_alpha[k:] + l_alpha[:k])) | dict(zip(u_alpha, u_alpha[k:] + u_alpha[:k]))

    encrypted = ""
    for i in range(len(s)):
        if s[i].isalpha():
            encrypted += alpha_map[s[i]]
        else:
            encrypted += s[i]
    return encrypted
