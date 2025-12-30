class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        left = 0
        max_profit = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right  # found a lower price

            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)

        return max_profit

# Problem: 121 - Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Approach:
#     - Two pointers: 'left' tracks the index of the lowest price seen so far (buy day)
#     - Iterate 'right' from index 1 to end as potential sell day
#     - If prices[right] is lower than prices[left], update left to right (better buy opportunity later)
#     - Otherwise, compute profit as prices[right] - prices[left]
#     - Track the maximum profit across all valid (left < right) pairs

# Time Complexity: O(n)
#     - Single pass through the array with O(1) operations per element

# Space Complexity: O(1)
#     - Only using constant extra space (left pointer and max_profit)

# Edge Cases Considered:
#     - len(prices) < 2 → return 0 (early guard clause)
#     - Prices strictly decreasing → left moves to end, profit remains 0
#     - Prices strictly increasing → left stays at 0, captures full rise
#     - Multiple local minima → left correctly jumps to lowest so far

# Alternative Approaches Considered:
#     - Brute force O(n²) → too slow
#     - Standard min_price tracking with min() → similar efficiency, slightly different style

# Learned:
#     - Greedy one-pass solution for "max profit with order constraint"
#     - Two-pointer style where buy pointer only moves on better opportunity
#     - This is NOT sliding window — it's greedy tracking of minimum