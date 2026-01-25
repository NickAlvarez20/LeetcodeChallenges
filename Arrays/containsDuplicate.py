from collections import Counter


# First solution

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        frequency_dict = Counter(nums)
        for key, value in frequency_dict.items():
            if value > 1:
                return True
        return False

# Second solution : Using prev index checks and sort


def containsDuplicate(self, nums: list[int]) -> bool:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False

# Third solution : Using a set (My initial approach) : Optimal approach average case is very fast because it returns true immediately upon finding the first duplicate

def containsDuplicate(self, nums: list[int]) -> bool:
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False

# Fourth solution: Checking length by using a set and if any are removed from the set array, compared to init array, then we have a dup in nums array


def containsDuplicate(self, nums: list[int]) -> bool:
    create_Set = set(nums)
    if len(create_Set) < len(nums):
        return True
    return False
