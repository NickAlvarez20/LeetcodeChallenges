class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split()[-1] 
        return len(last_word)

# Intuition
# For finding the length of the last word in the string. We need to remove the white space. Trailing and leading and isolate the final word. Using strip and split we can cleanly separate the words and access through indexing the last word within the string.
# Approach
# 1. The approach is to strip all the white space.
# 2. Next, we split the string into separate words.
# 3.Then we use a slice from the end to remove the last word. 
# 4.Then we return the length of the last word that is held within the variable. 
# Time complexity: O(n)
# 1. Strip method scans the string from both ends to remove the white space. O(n)
# 2.Split method without arguments iterates the entire string to find white space boundaries. O(n)
# 3.Indexing with -1 and length are both O(1). 
# Space complexity: O(n)
#1. Split creates a list of words which in the worst case. (For example, single character words separated by spaces uses O(n)  space. 
#2. The stripped string is temporary, but also O(n) in the worst case. 
#3.Overall space complexity. O(n) 
# Alternative methods. 
# 1.Optimal solution - Iterate from the end. O(n) time and O(1) space 
# - Create a variable that starts with the length minus 1. A while loop that skips trailing spaces and then count the characters of the last word.
# - 2. Use R split. Split from the right, ignoring trailing spaces. Clean one liner using Pythons built-in string methods. Or split. Automatically handles trailing spaces, unlike regular split. Very readable and concise. Time complexity: O(n) Space O(n)