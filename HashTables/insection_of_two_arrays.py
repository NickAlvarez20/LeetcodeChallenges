class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        dict_count = dict()

        if len(nums1) <= len(nums2):
            shorter, longer = nums1, nums2
        else:
            shorter, longer = nums2, nums1

        for i in shorter:
            dict_count[i] = dict_count.get(i, 0) + 1

        for num in longer:
            if num in dict_count and dict_count[num] > 0:
                result.append(num)
                dict_count[num] -= 1
        return result

# # Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
# Utilize a frequency counter or a dictionary to keep track of key value pairs This one is mostly about frequency and intuition 

# # Approach
# <!-- Describe your approach to solving the problem. -->
# So at first we got to lay the foundation creating a result and a dig count which will be a dictionary that stores the counts key value pairs. 2. Next we want to check if the length of any given array is greater so the main primary objective is to find the smaller array and then assign the smaller array to a shorter and longer variable. 3. Then we want to loop through the shorter and create a dictionary with a frequency count for each element within the shorter array . 4. Finally we want to loop through the longer array and check if the number within the longer array currently exists within the dictionary and the dictionary count is greater than zero this is important because we want to check while this condition is true. 5. If this condition is true we will append the current number that exists within longer into the result array. 6. Finally we want the dictionary count of that value to be subtracted by one and then we'll return the result.

# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# The time complexity for this it is O(N+M). Let him be the length of numb swollen and N be the length of nums 2 we loop through the shorter array to build the dictionary We loop through the longer array to find matches therefore the total is O of M + N which simplifies to O of N if the arrays are of similar size . 

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# The space complexity is O(M, N): The space complexity is of M, where we create a stores unique elements of the shorter array and worst case situation all elements are unique the dictionary will hold as many entries as there are elements in the shorter array Therefore the extra space scales linearly with the size of the smaller array. 

# # Code
# ```python3 []
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result = []
#         dict_count = dict()

#         if len(nums1) <= len(nums2):
#             shorter, longer = nums1, nums2
#         else:
#             shorter, longer = nums2, nums1

#         for i in shorter:
#             dict_count[i] = dict_count.get(i, 0) + 1

#         for num in longer:
#             if num in dict_count and dict_count[num] > 0:
#                 result.append(num)
#                 dict_count[num] -= 1
#         return result
        



        
