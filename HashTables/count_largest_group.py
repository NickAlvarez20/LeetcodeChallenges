# # Intuition
# So this problem was very confusing at first. After further clarification we need to use dictionary to keep track of the frequencies of the sum of individual numbers so we have to break down each digit into a single integer and each number within the array and then increment the frequency of that group. Holders for the initial state and then we can update it as we find the correlated groups.

# # Approach
# 1. So first we want to import default dictionary for placeholder values to initialize the state with all zeros and ensure that we're using integer. 
# 2. Then we want to iterate for the range from 1 to N + 1 Since arrays start at zero you want to update this from 1 to N + 1 to account for. 
# 3. Next we set up a temp and set it to numb and then set up a sum NUM variable that will hold the total sum for each temporary number that we are summing. 
# 4. Then we want to use a while loop condition greater than zero so that it exits as soon as the temporary variable hits a zero
# 5. Then we want to set up a Digit variable and set it equal to temp mod 10 to remove the last digit
# 6. Then we want to set up a sum num variable in add the digit For every iteration
# 7. Then we want to set up the temp variable and divide it with double division so we get the next number floored. 
# 8. Then once we have some NUM we want to assign it and update its frequency within the dictionary key
# 9. Then we want to find the highest frequency using the Max method in dictionary dot values and assign it to Max eval variable
# 10. Next we want to get a collection of all the keys that match the Max eval so we initialize Max keys and do this comprehension grabbing the key for the key value in dictionary.items if the value matches The Max value.
# 11. Finally we can return the length of the Max keys and this will give us the final result

# # Complexity
# - Time complexity: O(N)
# Digit Summation: The outer for loop iterates N times. For each number, the inner while loop extracts digits. The number of digits in any number up to N is proportional to \(\log_{10}(N)\). Since the problem limits N ≤ 10⁴, a number has at most 5 digits. Therefore, the inner loop runs a maximum of 5 times per number, which is a constant {O}(1) operation. This makes the overall loops take {O}(N) = {O}(N) time.Frequency Comparison: Finding the maximum value and filtering keys depends on the number of unique digit sums (K). The largest possible digit sum for N ≤ 10⁴ is 36 (from the number 9,999). Since K ≤ 37, checking the dictionary takes a fixed, constant O}(1) time.Total Time: {O}(N) + {O}(1) = O}(N).

# - Space complexity: O(1)
#  \(\mathcal{O}(1)\) (Constant Space)Dictionary Storage: While we iterate up to N, the defaultdict does not store N elements. It only stores the unique sums of the digits.Mathematical Boundary: For any input up to N = 10,000, the lowest possible digit sum is 1 and the highest is 36. This means the dictionary will never hold more than 37 key-value pairs, regardless of how large N gets within the problem constraints.Total Space: Because the auxiliary memory is strictly bounded by a tiny constant integer, the space complexity simplifies to {O}(1).

# Code
```python3 []
from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # iterate through the list and sum the digits, breaking them down to simplest form and append to dictionary
        dictionary = defaultdict(int)

        for num in range(1, n+1):
            temp = num
            sum_num = 0
            while temp > 0:
                digit = temp % 10
                sum_num += digit
                temp = temp // 10
            dictionary[sum_num] += 1
        
        # find highest frequency
        max_val = max(dictionary.values())

        # collection all keys that match
        max_keys = [key for key, value in dictionary.items() if value == max_val]

        return len(max_keys)



```