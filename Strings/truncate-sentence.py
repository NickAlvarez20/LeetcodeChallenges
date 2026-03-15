# Intuition: A sentence is a sequence of words separated by single spaces To truncate it to K words we can split the string into a list and keep only the first K elements joining these elements back with spaces reconstrucs the desired prefix 

# Approach:
# 1. Split the input string S into a list of individual words using the space character as a delimiter
# 2. Slice the results in the list to retrieve only the first K elements 
# 3. Join the slice list back into a single string separating each word with a space
# 4. Return to newly formed truncated sentence
# Complexity:
# Time: O(n)
# Splitting slicing and joining each touched the characters of the string once 
#
# Space: O(n)
# We temporarily store the words of the sentence in a list

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[:k])
