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

# The intuition is straightforward usually a set or a frequency dictionary We can also do previous index checks using a two pointers technique or we could do a length check of the set and compare it to the original. at first though it was saying frequency or set. 

# 1. The optimal algorithm uses a set so we declare a set in a variable called NUM set
# 2. Then we loop through using a for in loop
# 3. We check if numb in the set then we can return true
# 4. If the number is not in the set then we add it to the set using the method add and the NUM that we are currently on
# 5. If after all the evaluations are completed and we have not found the nonexisting in the set then we return false


# Analysis: The runtime was eight milliseconds it beats 81.13% and the memory is 31.25 megabits it beats 66.61% this places it in the top 10% of answers.

# We discussed the alternative solutions and just to reiterate we can do a frequency dictionary we can do a set we can do a set length compared to the original length and the last one we could do is a sort where we compare the next index to the previous index in a sorted array this will ensure that any value after the current index matches the current value of the index we are currently on that will indicate it's good. 
