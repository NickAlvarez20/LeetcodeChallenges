from collections import Counter


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        seen = set()
        for word in words:
            if word[::-1] in seen:
                count += 1
            else:
                seen.add(word)
        return count


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        seen = set()
        for word in words:
            if "".join(reversed(word)) in seen:
                count += 1
            else:
                seen.add(word)
        return count
