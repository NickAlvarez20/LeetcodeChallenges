# 392. Is Subsequence
# Easy
# Topics
# premium lock iconCompanies

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


# Constraints:

#     0 <= s.length <= 100
#     0 <= t.length <= 104
#     s and t consist only of lowercase English letters.


# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if t == "" and s == "":
            return True
        elif t == "" and s != "":
            return False
        matchingString = ""
        j = 0
        for char in t:
            if j < len(s) and char == s[j]:
                matchingString += char
                j +=1
        return matchingString == s


sol = Solution()
test1 = "ahbgdc"
subS = "acb"
result = sol.isSubsequence(subS, test1)
print(result)


# Intuition: Iterate through the substring and compare that to the characters currently in the given longer string. If the characters match then we want to build a new String. The reverse of this would be if the characters do not match we want to strip them away from the original string this would result in a comparable string where if it is in the correct order then removing characters from that string that are not matching will yield in a string that is in the correct order and we can use this to compare it to the original string It may have the same characters but they will not be in the correct order therefore we can Now compare that string in its currently proper order and compare that against the substring if those strings are matching then we have the correct order and it is true if they are not matching then we return false.

# Approach
# 1. The approach is to first use edge cases to determine if T and S are empty strings if they are then we return true because they are matching
# 2. Then we compare T as an empty string and S as not an empty string if this is true then we return false
# 3. We set up a matching string so we can build the new string with matching string set to an empty string
# 4. We set variable J to zero This will be a placeholder to go through the substring S
# 5. We loop through the characters in t
# 6. We create two conditions J is less than the length of S and chart equals S index axis J The first J is left the length of S means that we do not want to go past the length of S The second condition char is equal to the matching letter with an S does the current character in tea exactly match the next character we need from S This uses a two pointers approach to check in order character matches.
# Time complexity: O(n)
# 1. The major factor to consider is the for loop All other operations pale in comparison, We do one for loop and we compare if each time therefore the main factor to consider in the time complexity is the for loop and the for loop is simply the length of the given string therefore the time complexity is O(n)
# 
# Space complexity: O(n)
# 1. For the most part we have simple variables which are O(1)
# 2. We are building a string which is O(n)
# 3. Therefore the space complexity is O(n) for any given string length
# Alternative methods.
# 1. The alternative solution is looping through and checking with a pointer only This uses O(1) space instead of O(n)since we are not building a string. It checks the character currently in the iteration with the index value within the subsequence and this is how you can use it to go on the fly check with value index access.
