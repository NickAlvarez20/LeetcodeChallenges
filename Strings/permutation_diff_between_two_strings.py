# Intuition: Brute force approach pattern we can loop through and check where the match is equivalent within each string and then after we find a match we can subtract the indices

# Approach: So ideally we set a SU variable equal to zero and then we do a double nested for loop with I in range for Python to get the index specific value and then we do another for loop for J in range for the length of T we check if the charac= T once we find a match increment sum by the absolute value of the index I minus index J we break out and then we continue through this loop until we exhaust the range of length FS and we finally return the sum

# Complexity:
# Time: O(n^2)
# This brute force approach is O of N ^2, Quadratic time complexity since we use two nested loops to compare the elements in the first string with the elements in the 2nd string once we find the match we want to subtract therefore quadratic time complexity.
# 
# Space: O(1)
# The only thing we are really doing here is adding a sum variable the rest of it is iterating in place and not creating any extra space therefore it is constant space

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    sum += abs(i - j)
                    break
        return sum
