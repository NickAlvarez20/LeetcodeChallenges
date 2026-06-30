class Solution:
    def generateTheString(self, n: int) -> str:
        res = ""
        if n % 2 == 1:
            while n > 0:
                res += "a"
                n -= 1
        else:
            while n - 1 >= 1:
                res += "a"
                n -= 1
            if n <= 1:
                res += "b"
                n -= 1

        return res
