class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for index, val in enumerate(words):
            if val[0] != s[index]:
                return False
        return True

        