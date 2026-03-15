# Intuition: Find the maximum word count we must evaluate the length of each sentence in the list A sentence word count is determined by splitting it at every space character We use a running maximum to keep track of the largest word count found as we iterate

# Approach:
# 1. Initialize a variable maxlin to zero to track the highest count 
# 2. Iterate through the list of sentences using their index 
# 3. Split the current sentence into a list of words using the space delimiter 
# 4. Calculate the number of words in that specific sentence and store it in temp 
# 5. Compare the current count with Max LIN and update it if the new count is higher
# 6. Return the final Max Lin after all sentences have been processed
# Complexity:
# Time: O(n*m)
# We iterate through in sentences and splitting each sentence takes old M time where N is the number of characters
# 
#
# Space: O(m)
# Each split method creates a temporary list proportional to the number of words in that sentence 


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for i in range(len(sentences)):
            temp = len(sentences[i].split(" "))
            max_len = max(max_len, temp)
        return max_len
