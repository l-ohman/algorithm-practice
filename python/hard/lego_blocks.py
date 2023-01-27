# hard, dynamic programming
# https:#www.hackerrank.com/challenges/lego-blocks/problem
# explanation here - https://stackoverflow.com/a/15425302/18671364

mod = 1000000007  # to prevent int overflow (10 ** 9 + 7)

# tetranacci sequence: http:#oeis.org/A000078


def tetranacci(x):
    sequence = [1, 2, 4, 8]
    if x <= 4:
        return sequence[:x]
    for i in range(4, x):
        next_num = sum(sequence[i-4:])
        sequence.append(next_num)
    return sequence


# n: height, m: width
def legoBlocks(n, m):
    if m == 1:
        return 1
    elif n == 1:
        return 1 if m < 5 else 0

    # build an array of all wall combinations (where idx = width - 1)
    all_walls = tetranacci(m)
    for i in range(m):
        all_walls[i] = pow(all_walls[i], n, mod)

    solid_walls = all_walls.copy()
    # calculate 'invalid' combinations and subtract them
    for i in range(1, m):
        # iterate through everything smaller than i and subtract
        for j in range(i):
            left, right = solid_walls[j], all_walls[i - 1 - j]
            solid_walls[i] -= left * right
            solid_walls[i] = solid_walls[i] % mod
    return solid_walls[m-1]


def test():
    # [3,7,9,3375]
    print([legoBlocks(2, 2), legoBlocks(3, 2), legoBlocks(2, 3), legoBlocks(4, 4)])
    # [382238489,236807483]
    print([legoBlocks(924, 604), legoBlocks(505, 808)])
    # [0,0,1]
    print([legoBlocks(1, 33), legoBlocks(1, 812), legoBlocks(231, 1)])

if __name__ == "__main__":
    test()
