class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = word1
        right = word2
        index1 = 0
        index2 = 0
        result = ""
        while index1 < len(word1) and index2 < len(word2):
            result += left[index1]
            result += right[index2]
            index1 += 1
            index2 += 1
        return result + word1[index1:] + word2[index2:]


# Intuition
# The first thing that stands out intuitively is the 2 pointers approach You initially want to have one pointer starting at the beginning of the left and one at the beginning of the right as well as using indexes to increment and keep track of the pointer positions and then we can use a while loop using length

# Approach
# So the approach is to create a left and right pointer initialize the left pointer add to start of word 1 and initialize the pointer at the start of word 2 and then for the index 1 and two we set those equal to zero and we also want to create memory for the result variable. 
# After that we want to use a while loop And exit the loop when the condition length of word 1 and length of word 2 is less than the index during this process we append the letter associated with the left word index and the right word index and then increase and increment each index by one for each pass of the while loop.
# Finally we return the result and use pythonic slicing to grab the remainder of word 1 and word 2 whichever is going to be determined to be the longer word based on how the algorithm processes

# Complexity
# - Time complexity: O(M+N)
# Time complexity is O of M + N where M is the length of word 1 and N is the length of word 2 we narrate through each string exactly the same amount of times and then at the end we use pythonic slicing



# - Space complexity: Auxiliary Space is O(1) and Total Space is O(M+N)
# The auxiliary space complexity is O of one because we only use a constant number of pointers but the total space complexity is O of in to store the final merged output string. 


# # Code
# ```python3 []
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         left = word1
#         right = word2
#         index1 = 0
#         index2 = 0
#         result = ""
#         while index1 < len(word1) and index2 < len(word2):
#             result += left[index1]
#             result += right[index2]
#             index1 += 1
#             index2 += 1
#         return result + word1[index1:] + word2[index2:]



        
# ```