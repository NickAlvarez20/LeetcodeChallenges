class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # iterate backwards
        i = len(num)-1
        # store a count
        while i >= 0 and num[i] == "0":
            i -= 1
        
        return num[:i+1]
        