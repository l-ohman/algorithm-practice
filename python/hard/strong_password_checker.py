# https://leetcode.com/problems/strong-password-checker/

def strongPasswordChecker(password):
    l = len(password)

    missing_chars = 3
    if any(char.isupper() for char in password):
        missing_chars -= 1
    if any(char.islower() for char in password):
        missing_chars -= 1
    if any(char.isdigit() for char in password):
        missing_chars -= 1

    # check for repeating chars
    changes = 0
    change_or_remove_1 = change_or_remove_2 = 0

    i = 2
    while i < l:
        if password[i] == password[i-1] == password[i-2]:
            length = 2
            while i < l and password[i] == password[i-1]:
                length += 1
                i += 1
            changes += length//3
            if length % 3 == 0:
                change_or_remove_1 += 1
            if length % 3 == 1:
                change_or_remove_2 += 1
        else:
            i += 1

    # the trickest part - decreasing changes based on what can be removed instead
    if l > 20:
        removals = l - 20

        # case 1: "aaa" — straightforward
        case1 = min(removals, change_or_remove_1)
        # case 2: "aaaa" — we divide by 2 because it takes 2 deletions to resolve each violation
        case2 = min(max(removals - change_or_remove_1, 0),
                    change_or_remove_2 * 2) // 2
        # case 3: "aaaaa" — account for cases 1 and 2, and use remaining deletions to handle this
        # we divide by 3 for same reason as case 2 — it takes 3 deletions to resolve each violation
        case3 = max(removals - change_or_remove_1 -
                    2 * change_or_remove_2, 0) // 3

        changes -= case1 + case2 + case3

    # returns based on length
    if l < 6:
        return max(missing_chars, 6-l)
    elif l <= 20:
        return max(missing_chars, changes)
    else:
        return removals + max(missing_chars, changes)


def test():
    cases = {
        "aA1": strongPasswordChecker("aA1") == 3,
        "1337C0d3": strongPasswordChecker("1337C0d3") == 0,
        "aaa123": strongPasswordChecker("aaa123") == 1,
        "aaa111": strongPasswordChecker("aaa111") == 2,
        "bbaaaaaaaaaaaaaaacccccc": strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc") == 8,
    }
    failed = []
    for password, result in cases.items():
        if not result:
            failed.append(password)
    if len(failed) == 0:
        failed.append("None!")
    print("Failed:", " | ".join(failed))


test()
