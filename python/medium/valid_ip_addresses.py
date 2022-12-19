# string / medium
# input: string of length 12 or smaller, only ints
# output: fn that returns an array of all possible IP addresses by inserting 3 "."s

# assumptions:
# IP is not valid if it contains a leading 0 (such as "00" or "01")
# each individual integer must be less than 255

# apparently is O(1) time | O(1) space
def validIPAddresses(string):
    ips_found = []

    for i in range(1, min(len(string), 4)):
        potential_ip = ["", "", "", ""]
        if not is_part_valid(string[:i]):
            continue
        potential_ip[0] = string[:i]

        for j in range(i + 1, min(len(string), i + 4)):
            if not is_part_valid(string[i:j]):
                continue
            potential_ip[1] = string[i:j]

            for k in range(j + 1, min(len(string), j + 4)):
                if not (is_part_valid(string[j:k]) and is_part_valid(string[k:])):
                    continue
                potential_ip[2] = string[j:k]
                potential_ip[3] = string[k:]

                ips_found.append(".".join(potential_ip))

    return ips_found


def is_part_valid(string):
    if int(string) > 255:
        return False
    elif len(string) > 1 and string[0] == "0":
        return False
    else:
        return True
