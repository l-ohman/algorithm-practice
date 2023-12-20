# https://leetcode.com/problems/buy-two-chocolates/


# first attempt without sorting - beats 45% time and 24% memory
def buyChoco(prices, money):
    cheap = max(prices[0], prices[1])
    cheapest = min(prices[0], prices[1])
    for i in range(2, len(prices)):
        if prices[i] < cheap:
            if prices[i] < cheapest:
                cheap = cheapest
                cheapest = prices[i]
            else:
                cheap = prices[i]
    remaining = money - (cheap + cheapest)
    return remaining if remaining >= 0 else money


# second attempt, using sorting - beats 99.65% time and 23% memory
def buyChoco(prices, money):
    prices.sort()
    remaining = money - prices[0] - prices[1]
    return remaining if remaining >= 0 else money
