from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:

        count_digits = Counter(str(n))
        sum = 0
        for key, value in count_digits.items():
            sum += int(key) * int(value)
        return sum
