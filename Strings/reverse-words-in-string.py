class Solution:
    def reverseWords(self, s: str) -> str:
        split_str = s.split(" ")
        result = []
        for word in split_str:
            result.append(word[::-1])
        return " ".join(result)
