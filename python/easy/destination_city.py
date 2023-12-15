# https://leetcode.com/problems/destination-city/
from collections import defaultdict


# First attempt - 44% time complexity and 45% space complexity
def destCity(paths):
    # key as a city, val as boolean if it has an outgoing path
    has_outgoing = defaultdict(lambda: False)
    for path in paths:
        city_from, city_to = path[0], path[1]
        has_outgoing[city_from] = True
        if city_to not in has_outgoing:
            has_outgoing[city_to] = False
    for city, outgoing in has_outgoing.items():
        if not outgoing:
            return city


# Second attempt - 74% time complexity and 45% space complexity
def destCity2(paths):
    all_cities, has_outgoing = set(), set()
    for path in paths:
        all_cities.add(path[0])
        all_cities.add(path[1])
        has_outgoing.add(path[0])
    return (all_cities - has_outgoing).pop()


# Third attempt - 82% time complexity and 45% space complexity
def destCity3(paths):
    has_outgoing = set()
    for path in paths:
        has_outgoing.add(path[0])
    for path in paths:
        if path[1] not in has_outgoing:
            return path[1]
