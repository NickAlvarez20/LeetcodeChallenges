# Intuition: To reverse a prefix we first need to locate the first occurrence of the target character once found we treat the segment as a prefix and flip it If the character doesn't exist the string remains unchanged

# Approach:
# 1.  Check if target character CH exists in the word if not return their original word immediately
# 2. Iterate through the string using enumerate to track both the current character and its index 
# 3. Identified the first match where the current character equals ch
# 4. Slice the string from the beginning up to and including that index 
# 5. Reverse this slice using pythons reverse string syntax
# 6. concatenate the reverse prefix with the remaining part of the string and return the result 
# Complexity:
# Time: O(n)
# Searching for the character in slicing and reversing the string both take linear time relative to the length of the word 
# 100% best answer, beats 100%
#
# Space: O(n)
# Python strings are immutable so creating the new reverse string requires space for N characters


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for index, value in enumerate(word):
            if ch not in word:
                return word
            if value == ch:
                sliced_str = word[: index + 1]
                return sliced_str[::-1] + word[index + 1 :]
