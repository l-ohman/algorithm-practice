# matrix | easy
# input: (knight and king)'s positions, as: [int (rank), str (file)]
# output: "King" if knight is attacked, "Knight" if king is attached, "None" if neither

def knight_vs_king(knight, king):
    fileMap = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8
    }
    dx = fileMap[knight[1]] - fileMap[king[1]]
    dy = knight[0] - king[0]

    # alt method for dx: 'ord' fn returns unicode val for the letter ("A": 65, "B": 66, etc.)
    # we only need the difference, so the actual number would not matter here
    # dx = ord(knight[1]) - ord(king[1])

    # squaring before addition makes sum more reliable for comparisons
    d = dx ** 2 + dy ** 2 

    if d < 3: return "King"
    elif d == 5: return "Knight"
    else: return "None"


if __name__ == "__main__":
    print(knight_vs_king([5, "E"], [6, "F"]))  # King
    print(knight_vs_king([3, "E"], [4, "G"]))  # Knight
    print(knight_vs_king([1, "H"], [3, "H"]))  # None
