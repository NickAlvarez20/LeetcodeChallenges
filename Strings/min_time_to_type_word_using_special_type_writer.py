class Solution:
    def minTimeToType(self, word: str) -> int:
        count = 0
        current_char = ord("a")
        for char in word:
            conv_to_ord = ord(char)
            distance = abs(current_char - conv_to_ord)
            curr_min = min(distance, 26 - distance)
            count += curr_min + 1
            current_char = ord(char)
        return count


test = Solution()


print(test.minTimeToType("zjpc"))
