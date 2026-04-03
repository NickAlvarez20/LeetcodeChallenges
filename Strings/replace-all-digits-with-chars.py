import string
class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(char, digit):
            return chr(ord(char) + int(digit))
        
        res = ""

        for i in range(len(s)):
            if s[i].isdigit():
                res += shift(s[i-1], s[i])
            else:
                res += s[i]
        return res
        