from collections import Counter


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        result = []

        freq_dict = Counter(s)

        for key, val in freq_dict.items():
            if key:
                result.append(key)
        return len(result)
