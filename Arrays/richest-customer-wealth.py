# Intuition
# Intuitively what I look at is the brute force approach where there is a nested array within the array and it is as simple as using the sum function method with a brute force approach with I and J and adding it to a new result

# Approach
# So the approach is to set up a result variable set it equal to an empty array create a subarray sum variable set it equal to zero and then we loop through for I in range for J in range pattern while each time we reset the sum to 0 for each nested array. Then we simply use the sum method and the label accounts I which gets the current sub array and sums and then it gives us a value and then we result append that to the new array. Finally we return the Max of that new result array and this will give us the Max value.

# Complexity
# - Time complexity: O(m^2 * n)
# The outer loop runs \(m\) times (where \(m\) is the number of customers). The inner loop also runs \(m\) times. Inside the inner loop, Python's built-in sum() function takes \(O(n)\) time (where \(n\) is the number of banks) to traverse the sub-array.


# - Space complexity: O(m)
# The space complexity is linear with respect to the number of customers. This is because we create a new result array that stores exactly one total wealth integer for each of the \(m\) customers in the input.


# Code
# ```python3 []
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         result = []
#         sub_array_sum = 0
#         for i in range(len(accounts)):
#             sub_array_sum = 0
#             for j in range(len(accounts)):
#                 sub_array_sum = sum(accounts[i])
#             result.append(sub_array_sum)
#         return max(result)

# ```


# Optimal approach


# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         max_wealth = 0

#         for customer in accounts:
#             # sum(customer) takes O(n) time
#             current_wealth = sum(customer)
#             # Update the max wealth found so far
#             max_wealth = max(max_wealth, current_wealth)

#         return max_wealth
