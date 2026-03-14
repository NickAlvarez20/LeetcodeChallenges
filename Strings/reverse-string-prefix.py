class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        slice = s[:k]
        reversed_slice = slice[::-1]
        return reversed_slice + s[k:]
