from collections import Counter


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting_cities = set()
        result = []

        for item in paths:
            starting_cities.add(item[0])

        for city in paths:
            if city[1] not in list(starting_cities):
                return city[1]
