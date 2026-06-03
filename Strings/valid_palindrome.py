import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(result) - 1
        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True


        

# Intuition
# Iterate through the entire string using two pointers. Starting from the left and the right, comparing each character, if they're a valid match all the way until the middle, then they are a valid palindrome. This requires stripping of all non alphanumeric characters and any sort of weird spacing or commas. 

# Approach
# 1. Import the regular expressions module and set a variable called result and then perform regex to remove all of the non alphanumeric characters from the string and convert to lower case using the lower method. 
# 2. Using two pointers initialize left variable to zero and right. To the length of the result minus one, so we start at the end with the right pointer. 
# 3. While left is less than right, we want to compare the result using index notation to make sure that result left pointer does not equal right pointer. If we see that there's a mismatch of any of these as we iterate through, then we know that there is no palindrome. 
# 4. Increment left by one for each iteration and reduce the right pointer minus 1 to make sure that as we go from left to right; we are matching the correct letters for any given string. 
# 5. Return true if all the letters are matching, indicating a valid palindrome. 

# Time Complexity: O(n)
# - Using regex and the lower method is O(n) as they scan the string.
# - While loop iterates through the entire length of any given string indicating length of O(n) for every letter in the string. 
# - Incrementing and decrementing the left and right variables is very simple, O(1)
# - Overall: O(n) for the length of any given string

# Space Complexity: O(n)
# - Pythons regex uses O(n) space internally to properly update the string. This creates a copy. Python strings are immutable.
# - Left and right variables store the beginning and end which is O(1) space. 
# - The while loop doesn't cost any extra space Beyond a few variables. 
# - Overall: O(n) auxiliary space. 

# Alternative methods:
# Approach 1 (Current method): Clean the string by removing non-alphanumeric characters and converting to lowercase with regex, then use two pointers from both ends to check if characters match.
# Approach 2 (two pointers without extra string): Move left from the start and right from the end of the original string, skipping non-alphanumeric characters on the fly and comparing only letters/numbers (ignoring case).