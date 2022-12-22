# hash table | medium
# input: int "a"
# output: roman numeral representation of int "a"

roman_letters = ["M", "D", "C", "L", "X", "V", "I"]
roman_numbers = [1000, 500, 100, 50, 10, 5, 1]


def int_to_roman(input):
    output = ""
    for i in range(0, len(roman_numbers), 2):
        count = input // roman_numbers[i]
        input = input % roman_numbers[i]

        if count == 4 or count == 9:
            output += roman_letters[i] + roman_letters[i - count // 4]
            continue
        elif count >= 5:
            output += roman_letters[i - 1]
            count -= 5
        output += roman_letters[i] * count

    return output


if __name__ == "__main__":
    print(f"\nTesting fn '{int_to_roman.__name__}'...")
    test_cases = {
        549: "DXLIX",
        23: "XXIII",
        94: "XCIV",
        1994: "MCMXCIV"
    }
    passing = True
    for num in test_cases:
        val = int_to_roman(num)
        if val != test_cases[num]:
            passing = False
            print(f"  Incorrect value for {num}; Expected: '{test_cases[num]}' | Actual: '{val}'")
        else:
            print(f"  Correct value for {num}: '{test_cases[num]}'")
    if passing: print("All tests passing!")
    else: print(f"Tests failed")
