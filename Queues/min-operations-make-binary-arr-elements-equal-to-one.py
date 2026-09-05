# # Intuition
# The optimal solution relies on a cue. The straightforward intuition is to use a brute force approach.

# # Approach
# 1. First, in order to make sure that all the elements in the array are equal to 1, we want to create a variable called total sum and set it equal to the sum of the entire nums array.
# 2. Then we have to implement a variable counter that will be utilized to count and update.
# 3. So first, we want to see if the array is already equal to all ones. If so, we simply utilize the total sum, set it equal to the length of nums, and if it's good to go, we can return zero. Returning 0 is important because there are no steps to increment in the counter, therefore nothing was done during processing, therefore return 0.
# 4. Else we want to start a for loop for the range 0 to the length of nums minus 2. We want to iterate just two positions before the end of the nums array. This is important because we will be looking at the current index plus the next two positions to the right. Therefore, we must make sure no index out of bounds occurs by subtracting two from the length of nums.
# 5. Then I will check if the current value is equal to zero.
# 6. If it is equal to 0, we can start another for loop for j in range to i, considering i+3 is necessary because the for loop is inclusive.
# 7. Then we can check conditions if the j value is equal to 0 we want to flip it otherwise we can keep it as a 0.
# 8. For each part of this process when it identifies a zero, then we flip the ones and we're going to increase the counter by one.
# 9. Then for the end, we want to check if there's any zeros within the nums for this entire iteration. This will have processed it correctly, so if we look inside using for in and we find a zero, we can return negative one; otherwise, we can return the counter.

# # Complexity
# - Time complexity: O(N)
# Even though there is a nested for loop, four in range to i to i plus three, the inner loop always runs exactly three times regardless of how large the input array is. Because three is a constant number, the work done inside the inner loop is O of one constant. Sum of nums takes O of n time, the outer loop runs up to n minus two times, performing a max of three ops per iteration. This takes O of n time. Combining these O of n plus O of n equals O of n.

# - Space complexity: O(1)
# The space complexity is equal to O of 1. Since we are mutating the array in place, there's no other extra space being allocated. Bits are simply being flipped.

# Code


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        counter = 0
        if total_sum == len(nums):
            return 0
        else:
            for i in range(0, len(nums)-2):
                if nums[i] == 0:
                    for j in range(i, i+3):
                        if nums[j] == 0:
                            nums[j] = 1
                        else:
                            nums[j] = 0
                    counter += 1
 
        if 0 in nums:
            return -1
        else:
            return counter
