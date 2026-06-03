from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq_map = Counter(s)
        compare_set = set(freq_map.values())

        if len(compare_set) == 1:
            return True
        else:
            return False
