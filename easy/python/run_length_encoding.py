# string / easy
# input: non-empty string
# output: the input's "run-length encoding" (AAAABB => 4A2B)

# O(n) time | O(n) space
def run_length_encoding(string):
    char = string[0]
    counter = 0
    output = ""

    for i in range(len(string)):
        if string[i] != char or counter == 9:
            output += str(counter) + char
            char = string[i]
            counter = 1
        else:
            counter += 1
    output += str(counter) + char

    return output
