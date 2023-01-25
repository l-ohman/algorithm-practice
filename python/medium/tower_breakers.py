# easy - but i have marked as medium due to complication of 'game' in question.
# (the way this problem is written makes it very difficult - even the solution can be a single line of code.)
# https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/problem

# if number of towers is even, the player who moves first loses.
def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    return 1
