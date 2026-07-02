from collections import Counter


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_counts = Counter(word)
        count = 0

        for char in set(word):
            if char.islower():
                uppercase_mirror = char.upper()
                if uppercase_mirror in char_counts:
                    count += 1
        return count


# Optimal Solution:
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Fixed-size arrays of size 26 (all initialized to False)
        # Tracks if we have seen lowercase and uppercase versions of letters
        seen_lower = [False] * 26
        seen_upper = [False] * 26

        # Single pass through the string: O(n)
        for char in word:
            if char.islower():
                # Convert 'a'-'z' to an index 0-25
                index = ord(char) - ord("a")
                seen_lower[index] = True
            else:
                # Convert 'A'-'Z' to an index 0-25
                index = ord(char) - ord("A")
                seen_upper[index] = True

        # Count pairs where both lowercase and uppercase were seen: O(1)
        special_count = 0
        for i in range(26):
            if seen_lower[i] and seen_upper[i]:
                special_count += 1

        return special_count


# # Intuition
# The problem asks us to count the number of "special" characters, defined as lowercase letters that also appear in their uppercase form within the given word. To check for this quickly, we can extract the unique characters from the string and use a frequency map or lookup table to see if both casing variations exist.

# # Approach
# 1. Initialize a `Counter` dictionary `char_counts` of the `word` to enable \(O(1)\) lookup for any character.
# 2. Initialize a running `count` variable to 0.
# 3. Iterate through a `set(word)` to process each unique character exactly once, avoiding duplicate calculations.
# 4. For each character, check if it is lowercase using `.islower()`.
# 5. If it is lowercase, find its uppercase variant using `.upper()` and check if that uppercase letter exists in our `char_counts` map.
# 6. If both variants are present, increment `count` by 1.
# 7. Return the final `count`.

# # Complexity
# - Time complexity:
# \[O(N)\]
# Where \(N\) is the length of the string `word`. Creating the `Counter` and the unique `set` both take \(O(N)\) time. The loop runs at most \(U\) times where \(U\) is the number of unique characters (\(U \le 52\)). The lookup operations inside the loop take \(O(1)\) average time, resulting in an overall linear time complexity.

# - Space complexity:
# \[O(1)\]
# The `char_counts` dictionary and the unique character `set` store at most 52 elements because the input is restricted to uppercase and lowercase English letters. Since this storage space is bound by a fixed constant, the auxiliary space complexity is \(O(1)\).

# # Code
# ```python3 []
# from collections import Counter

# class Solution:
#     def numberOfSpecialChars(self, word: str) -> int:
#         char_counts = Counter(word)
#         count = 0

#         for char in set(word):
#             if char.islower():
#                 uppercase_mirror = char.upper()
#                 if uppercase_mirror in char_counts:
#                     count += 1
#         return count
# ```
