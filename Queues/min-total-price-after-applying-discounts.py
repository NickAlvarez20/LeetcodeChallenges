# # Intuition
# So after reading the description for minimum total price after applying discounts, I wanted to brute force the solution, basically performing an iteration for the length of the discounts and doing index matching using zip while it's possible. I found a more optimal solution using a queue after thoroughly reviewing and understanding the pattern.

# # Approach
# 1. from collections import DQ
# 2. I want to start with sorting, so I create sorted prices and sorted discount. I perform a sort using a shallow copy, passing in prices and discounts, and setting reverse equal to true. That's why it's from ascending to descending order.
# 3. SetupTotal = 0. Then, I'm going to create two queues: queuePrices set to sortedPrices, passing sortedPrices as the argument. Then, creating queueDiscounts set to sortedDiscounts. I have initialized both queues properly.
# 4. While Q discounts and Q prices exist, I initialize the while loop. I have to make sure both exist because if one of those conditions is false, then I need to exit the loop because either one is shorter than the other and vice versa.
# 5. For the first operation within the while queue, I want to create a curd discount and pop left from the curd discount and store that in the variable.
# 6. For the second variable, CurpPrice, I want to pop the left value from the cube prices and store that in a variable.
# 7. Now, I want to perform the calculation for the discounted price so I can pass the current price times 100 minus the current discount and divide that by 100.
# 8. Then I can add to the total this current discounted price.
# 9. Now that I've completed most of the logic for the length of either/or queue discounts or queue prices, I can add to the total the remaining that exists within queue prices, adding sum as the method and passing the rest of queue prices because the queue has essentially used pop left to remove all the values, so I can just sum this entire queue prices. Pretty clever.
# 10. Then I can return the total and this will solve the problem.

# # Complexity
# - Time complexity: O(NlogN + MlogM)
# For time complexity, the bottleneck of this solution is the sorting step. Sorting the prices array takes O(n log n) time and sorting the discounts array takes O(m log m) time, where n and m are their respective lengths, since the sorting within Python uses timsort. Now converting them to dQ takes linear time, O(n + m). The while loop runs for a minimum of n or m steps, doing O(1) constant time, and pop left operations. Finally, summing up the remaining prices takes at most O(n) time. Combining these, the overall time complexity is dominated by the sorting, which is O(n log n + m log m).

# - Space complexity: O(N+M)
# For space complexity, we are creating two shallow copies for the sorted list, taking O(n) and O(n) time. We then load them into DQs, which takes another O(n) and O(n) space. The remaining variables use constant auxiliary space. This gives us a total space complexity of O(n) + O(M).

# - How to improve
# If I were to optimize this for a production environment or target constraints, and I could actually reduce the space complexity to all of one auxiliary space, instead of creating new sorted lists and allocating memory for DQs, I could sort the input arrays in place using sort, reverse, is it true? And I could replace the queues entirely by using a simple two-pointer approach or iterating with zip, eliminating all extra memory allocations.

# Code
from collections import deque

class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        sorted_prices = sorted(prices, reverse=True)
        sorted_discount = sorted(discounts, reverse=True)
        total = 0

        queue_prices = deque(sorted_prices)
        queue_discounts = deque(sorted_discount)

        while queue_discounts and queue_prices:
            curr_discount = queue_discounts.popleft()
            curr_price = queue_prices.popleft()
            discounted_price = curr_price * (100-curr_discount) / 100
            total += discounted_price

        total += sum(queue_prices)
        return total
