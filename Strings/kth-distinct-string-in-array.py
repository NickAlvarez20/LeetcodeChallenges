from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        result = []
        final = []
        for key, value in counts.items():
            if value == 1:
                result.append(key)
        for i in range(1, len(result) + 1):
            if i == k:
                final.append(result[i - 1])
        return "".join(final)
