# Commonly used in finding sub-arrays with specific sum, finding the longest substring with unique characters, or solving problems that require a fixed-size window to process elements efficiently
# Substrings, subarrays, or windows
# Specifically commonly used for problems like finding subarrays with a specific sum, finding the longest substring with unique characters, or solving problems that require a fixed-size window to process elements efficiently.

# The main idea is to the use the results of the previous window to do computations for the next window


def maxSum(arr, k):
    n = len(arr)

    if n <= k:
        print("Invalid")
        return -1

    window_sum = sum(arr[:k])

    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)
    
    return max_sum