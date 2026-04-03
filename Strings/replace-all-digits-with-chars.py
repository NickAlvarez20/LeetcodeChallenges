class Solution:
    def replaceDigits(self, s: str) -> str:
        # create helper function
        def shift(char, digit):
            return chr(ord(char) + int(digit))
        
        res = ""

        for index, val in enumerate(s):
            if val.isdigit():
                res += shift(s[index-1], val)
            else:
                res += val
        return res
    
# alternative variation using range:
class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(char, digit):
            return chr(ord(char)+int(digit))
        res = ""
        for i in range(len(s)):
            if s[i].isdigit():
                res += shift(s[i-1], s[i])
            else:
                res += s[i]
        return res
        