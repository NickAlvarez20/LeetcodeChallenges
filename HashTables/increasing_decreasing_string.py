from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        res = []
        char_counts = Counter(s)
        total_chars = len(s)

        while total_chars > 0:
            for char_code in range(ord("a"), ord("z") + 1):
                char = chr(char_code)
                if char_counts[char] > 0:
                    res.append(char)
                    char_counts[char] -= 1
                    total_chars -= 1
            for char_code in range(ord("z"), ord("a") - 1, -1):
                char = chr(char_code)
                if char_counts[char] > 0:
                    res.append(char)
                    char_counts[char] -= 1
                    total_chars -= 1

        return "".join(res)


# Optimal Approach:


class Solution:
    def sortString(self, s: str) -> str:
        char_counts = Counter(s)
        # Get sorted list of unique characters present in s
        unique_chars = sorted(char_counts.keys())
        res = []

        while char_counts:
            # Step 1-3: Smallest to largest
            for char in unique_chars:
                if char_counts[char] > 0:
                    res.append(char)
                    char_counts[char] -= 1

            # Step 4-6: Largest to smallest
            for char in reversed(unique_chars):
                if char_counts[char] > 0:
                    res.append(char)
                    char_counts[char] -= 1

            # Clean up unique_chars to skip elements that reached 0
            unique_chars = [c for c in unique_chars if char_counts[c] > 0]

        return "".join(res)


# # Intuition
# The problem requires us to repeatedly pick characters in a strict ascending order, followed by a strict descending order, until all characters are used. A frequency map helps us keep track of how many times each character appears so we can systematically pick them out in waves.

# # Approach
# 1. Count the occurrences of each character in the string using a frequency map (`Counter`).
# 2. Maintain a variable `total_chars` to track how many characters are left to process.
# 3. Use a `while` loop that runs until `total_chars` reaches 0.
# 4. Inside the loop, simulate the **ascending wave** by iterating from character 'a' to 'z'. If a character is available, append it to the result list, decrement its frequency, and reduce `total_chars`.
# 5. Next, simulate the **descending wave** by iterating backward from 'z' to 'a'. Apply the same logic to pick available characters.
# 6. Finally, join the list of characters into a single string and return it.

# # Complexity
# - Time complexity:
# \[\mathcal{O}(n)\]
# Although there are nested loops, the inner loops always run a fixed 26 times (from 'a' to 'z'). The outer loop runs proportional to the number of characters. Each character in the string is visited and processed a constant number of times.

# - Space complexity:
# \[\mathcal{O}(1)\]
# The `Counter` map stores at most 24 to 26 unique lowercase English letters. The space required for the frequency tracking remains constant regardless of how long the input string grows.

# # Code
# ```python3 []
# from collections import Counter

# class Solution:
#     def sortString(self, s: str) -> str:
#         res = []
#         char_counts = Counter(s)
#         total_chars = len(s)

#         while total_chars > 0:
#             # Ascending wave: 'a' to 'z'
#             for char_code in range(ord("a"), ord("z")+1):
#                 char = chr(char_code)
#                 if char_counts[char] > 0:
#                     res.append(char)
#                     char_counts[char] -= 1
#                     total_chars -= 1

#             # Descending wave: 'z' to 'a'
#             for char_code in range(ord("z"), ord("a")-1, -1):
#                 char = chr(char_code)
#                 if char_counts[char] > 0:
#                     res.append(char)
#                     char_counts[char] -= 1
#                     total_chars -= 1

#         return "".join(res)
# ```
