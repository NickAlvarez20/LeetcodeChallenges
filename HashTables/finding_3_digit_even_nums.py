class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        i = 100
        res = []
        while i < 1000:
            num_str = str(i)
            if (
                int(num_str[0]) != 0
                and int(num_str[0]) in digits
                and int(num_str[1]) in digits
                and int(num_str[2]) in digits
                and int(num_str) % 2 == 0
            ):
                res.append(int(num_str))
            i += 1
        return res
