# # Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->

# # Approach
# <!-- Describe your approach to solving the problem. -->

# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->

# # Code
# ```python3 []
# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         # create length and init zero based array 
#         length = len(boxes)
#         result = [0] * length

#         for i in range(length):
#             for j in range(length):
#                 if boxes[j] == '1':
#                     result[i] += abs(i-j)
#         return result
        



        
# ```

# Unfinished