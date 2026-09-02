# # Intuition
# I would want to use two pointers and sorting in order to efficiently handle this with a while loop condition and max.

# # Approach
# 1. First, I set up sorted pairs and I sort the numbers by creating a shallow copy.
# 2. Then I declare left and right, setting left equal to 0 and right equal to the end position of the nums array.
# 3. Then I set totalSum to 0 and declare an emptyResultArray variable.
# 4. I initialize a while loop for the condition left is less than the right pointer.
# 5. Then the total sum is added from the sorted pairs of the left plus the sorted pairs of the right. This will give us the total sum for the current left and right position which indicates the max and the min; Based on the sorted array, allowing us to traverse and accommodate this algorithm efficiently.
# 6. Next, once we declare and sum the total sum, we can append that value to the result array and increment left and decrement right by 1 and reset total sum to 0 for each iteration.
# 7. Then we'll just return the max within the result, giving us the final solution.

# # Complexity: O(nlogn)
# - Time complexity: In step 1, when we sorted the nums array, the sorted function uses Timsort, which takes O(log n) time. The while loop runs O of n time because the pointers move inward in process divided by two pairs. Since O(n log n) grows faster than O(1), the sorting step dominates. Therefore, the total time complexity is O(n log n).

# - Space complexity: O(n)
# Since we are using the two pointers approach, the memory allocation is very efficient at constant O(1). We have the variables left, right, totalSumResult, and sortedPairs, which is a shallow copy. Therefore, the memory allocation is actually O(n) because we're building the result finally and we need to perform a max deduction on that. So it's actually O(1) for any given nums list as we create the result array that will grow with the size of the total pairs. So it could be O(n) or O(n) divided by 2, since we're basically logarithmically deducing the addition to the result array by n divided by 2. However, dividing by 2, n divided by 2 is a linear fraction, not logarithmic. In big O, we drop constants, so o n divided by 2 simplifies directly to o of n.

# Code

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_pairs = sorted(nums)
        left = 0
        right = len(nums) - 1
        total_sum = 0
        result = []

        while left < right:
            total_sum += sorted_pairs[left] + sorted_pairs[right]
            result.append(total_sum)
            left += 1
            right -= 1
            total_sum = 0
        
        return max(result)
