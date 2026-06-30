from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Create frequency
        freq_dict = Counter(arr)
        # Create a set
        seen = set()

        for key, val in freq_dict.items():
            if val not in seen:
                seen.add(val)
            else:
                return False
        return True


# Optimal, shorter solution

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_dict = Counter(arr)
        # If the number of unique counts matches the number of unique keys,
        # then all counts are unique.
        return len(freq_dict) == len(set(freq_dict.values()))
