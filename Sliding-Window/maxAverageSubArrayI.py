class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # find max average of given length k
        n = len(nums)

        window_sum = sum(nums[:k])

        max_sum = window_sum

        for i in range(n - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            max_sum = max(window_sum, max_sum)
        return max_sum / k


# Intuition:
# This problem asks to find a contiguous subarray. The keyword here is Contiguous sub array. Therefore we can use a sliding window to calculate the contiguous sub arrays find the maximum value and divide it by length K for any given array and we will find the maximum average. Another key insight is that a sub array has a maximum average if and only if it has a maximum sum. Therefore if we find the Max sum we can divide it by K and we'll find the maximum average.
#
# Approach:
# 1. First we define the class called Solution and then we create the function findmax average with the parameter itself nums as a list of integers K as an integer and it returns a float value
# 2. Then assign a variable called in to equal the length of any given array
# 3. Assign window sum equal to the method of the Python library su using NUM's array with a slice up to K
# 4. Assign Max sum with the window This initializes before the while loop and sets Max sum equal to the current window and it's sum
# 5. Initialize a 4 within the range N - K this will ensure that we traverse only until the window hits Max value
# 6. For each iteration assign window sum equal the current some value minus the current value at index position, The current value at this position, And add value one further This will increment the window thus causing the sliding window behavior intended. This will also correctly calculate the windows at each incremental window as we slide the window we store it inside of window sum
# 7. We need to update maxim for every iteration using the Max method in the Python library module Therefore we set maximum equal on each iteration and we compare the values of the current calculated window sum and we compare that with the Max sum This will allow us to identify whether or not the current maxim is greater than the current window some if it is we update Max with the greater of the two values thus the reasoning for the Max method
# 8. Finally we return the Max sum divided by K This will give the correct answer because we first need to find the backs some within each sliding window and then we can divide it by k. It's important to know that we could do this at every iteration but due to mathematics of computers and floating point precision they lose the floating point precision due to rounding errors within loops It's very important to be aware of this behavior otherwise calculate unexpected rounding errors Therefore you byte at the end just once optimizing performance.


# Time complexity: O(n)
# We have one for loop which is the largest coefficient within all the other factors therefore this is O of N time complexity
# Space complexity: O(n)
# The space complexity is O We are not adding on any extra arrays or data structures

# Analysis:
# The runtime is 62 milliseconds it beats seventy three point 15 Mcmurray is 28.90 megabytes it beats 48.21% displaces it in the top 40% of all solutions
# The hardest part is to visualize the algorithm and how to implement it but it's pretty cool once you start to see the removal of the first index that makes up the window and the addition of the last index therefore you're sliding the window

# Alternative solutions
# You could do a brute force approach two loops outer loop to pick the starting index and the inner loop to sum exactly K elements. Time complexity is N * K
# You could do binary search
# You could also do prefix some array approach instead of calculating the sum as you go you can preprocess the rate to create a prefix sum list prefix sum I stores the sum of all elements from index zero to I the sum of sub array of length K starting at index J can then be calculated in O of one time by subtracting prefix sum of J - 1 from prefix sum of J + K - 1 this is particularly useful if you need to query multiple different sub array links on the same data. 
