class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # I want to find numbers within a range so I need to 1 find the length of the array create a dictionary for that link and then check if the dictionaries values don't exist within that range

        length_nums = len(nums)
        dict_nums = {}
        arr_one = []
        result = []

        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1

        for i in range(1, length_nums + 1):
            arr_one.append(i)
        print(arr_one)

        for num in arr_one:
            if num not in dict_nums:
                result.append(num)

        return result


# # Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
# When first approaching the problem the thing that sticks out is to use a dictionary to create key value pairs Then we need to iterate over a range and identify within a new array that we create for the range which numbers are in that range array that don't exist within the dictionary

# # Approach
# <!-- Describe your approach to solving the problem. -->
# So 1. we need to create a length nums variable, a dictionary variable, an array variable, and a result variable. 2. Next we need a loop through for NUM innums and create a dictionary with these values using the dot get method. 3. Then we need to loop through the range from one to the length plus one and create a new array with all these values. 4. Then we need to loop through the numbers within the array and check if they exist as keys within the dictionary If they are not keys within the dictionary then we can add these numbers to the final result array.

# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
#  Each part of the algorithm utilizes O of N for any given array or dictionary as we simply iterate update and append. Therefore the time complexity is O of N.

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
#  The space complexity is only O of N for any given nums as we create a fixed size one dictionary one array one result array and a length nums variable This grows within the same scope as nums grows.

# # Note: You can delete the entire arr_one loop and just do this:
# for num in range(1, length_nums + 1):
#     if num not in dict_nums:
#         result.append(num)

# # Code
# ```python3 []
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

#         # I want to find numbers within a range so I need to 1 find the length of the array create a dictionary for that link and then check if the dictionaries values don't exist within that range

#         length_nums = len(nums)
#         dict_nums = {}
#         arr_one = []
#         result = []

#         for num in nums:
#             dict_nums[num] = dict_nums.get(num, 0) + 1

#         for i in range(1, length_nums+1):
#             arr_one.append(i)
#         print(arr_one)

#         for num in arr_one:
#             if num not in dict_nums:
#                 result.append(num)

#         return result


# ```
