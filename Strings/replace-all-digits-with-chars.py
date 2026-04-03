class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(char, digit):
            return chr(ord(char)+int(digit)) # have to convert to ord num, convert digit to int and add     
        res = ""
        for index, val in enumerate(s):
            if val.isdigit():
                res += shift(s[index-1], val)
            else:
                res += s[index]
        return res


        