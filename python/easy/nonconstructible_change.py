# easy, arrays

def nonConstructibleChange(coins):
    min_count = 0
    coins.sort()
    for coin in coins:
        if coin > min_count + 1:
            break
        min_count += coin
    return min_count + 1
