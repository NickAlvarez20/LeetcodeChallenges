class Solution:
    def finalString(self, s: str) -> str:
        result = ""
        for index, val in enumerate(s):
            if val != "i":
                result += val
            elif val == "i":
                result = result[::-1]
        return result
        