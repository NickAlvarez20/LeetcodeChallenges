class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        num_strings = 0
        for _, val in enumerate(patterns):
            if val in word:
                num_strings += 1
        return num_strings
        