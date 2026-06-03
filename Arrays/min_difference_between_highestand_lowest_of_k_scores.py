class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        # sort the list
        sortedNums = sorted(nums)
        sortedNums.reverse()
        min_sum = sortedNums[0]-sortedNums[1]
        return min_sum
# Naive approach using sort is correct intuition. However this was a naive approach for only uh K of equal to two or less so I had an edge case 1st where I would just set it equal to zero since a length of one is just zero and then we could do a sorted subtraction of the 2 1st indices but that would not result The correct answer for anything greater than K of equals 2.


class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))

# So we want to break this down into pieces what's the first part of the return statement it's this piece right here
# nums[i + k - 1] - nums[i] - This is the difference between the highest and lowest scores among these K students The final answer is the minimum value among all possible nums[i + k - 1] minus nums[i]i

# range(len(nums) - k + 1) = the total number of possible windows of size k than can fit inside the array


class Solution:
    def minimumDifference(self, nums, k):
        # abstract logic and clean code setting n to equal length of nums
        n = len(nums)
        # sort the nums array
        nums.sort()

        # Edge case: single element → difference is 0
        if k == 1:
            return 0
        # set sliding windows to index position of k-1 and subtract from nums[0] pos
        min_diff = nums[k - 1] - nums[0]  # first possible window
        # Slide window of size k across the sorted array
        for i in range(0, n - k + 1):
            # perform minimum check and update answer with sliding window
            # compare current window with our best so far
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])
        return min_diff


class Solution:
    def minimumDifference(self, nums, k):
        # abstract the logic
        lengthNums = len(nums)
        nums.sort()
        min_diff = nums[k-1]-nums[0] # declare 1st min
        # loop
        for i in range(1, lengthNums-k+1):
            min_diff = min(min_diff, nums[i+k-1]-nums[i])
        return min_diff

# Time complexity is O(nlogn):
# Sorting uses Tim sort which takes ON log N time which N is the length of the input array and the time complexity is dominated by the sorting step.
# Sliding window loop the for loop runs from 1 to N - K + 1 this is a single pass through the array taking O(n) time
# \(O(n\log n)+O(n)\), which simplifies to \(O(n\log n)\).


#Space complexity O (n) or O(log n)
# Space complexity depends on the implementation of the sorghing algorithm in language use typically Pythons list .sort tim sort requires of in additional space to store temporary data during the sorting process.
# Some versions of quicksorted heaps that may reduce this to oven login or O of one but since this is pythonic syntax Ovid is the standard answer for space.
# The variables lengthNums, min_diff, and i use \(O(1)\) auxiliary space. 

# The intuition is to use a sliding window approach to calculate from the K given value to determine the sliding window length and the calculation from the last element in the window to the first or vice versa. It's also good to be able to sort so that's part of the intuition. 

#1. So algorithm works by setting a variable called length norms equal to the length of noms this is good for abstracting out the logic to make the code easier to read and implement.
#2. The second part of the logic is to sort the array in ascending order This is important to know because if you sort it in descending order you're going to have to change the implementation of min diff variable.
#3. Next thing we want to do is set a variable called min difference equal to the nums index of K - 1 this is important because we are indexing starting at 0 in computer science therefore we must subtract one from the current index of K to get the appropriate window size.
#- Then we subtract nums starting position this will allow us to set the minimum difference at the start of the loop to the first window size it's also good for understanding the variable of the implementation of min difference within the loop to update it.
# 4. Then we loop through for I in range of one to the length of nums - K plus one So what this does is it loops until the correct final position that will allow us to analyze the first position of the window and the last position of the window without exceeding the entire length of the nums array This is important because this allows us to keep the window within the correct size of the array while analyzing based on K size the correct window size as well as the correct stoppage of the window.
# 5. Next we set min difference within the loop to auto update based on what it finds based on the mathematical equation we implement within min diff So we use min which is a method to find the minimum within the evaluator expression within the parentheses. Now we set the first argument as min difference so this stores the current argument that we are evaluating and then the 2nd one that we want to consider within the min method argument is nums of I + K - 1 which is going to take the index that we are on add in the total length of the current K variable and subtract 1 to appropriately update the window to the last index of the window and we subtract that from the nums index Now it's important to know that we are using bracket notation so for the bracket we evaluate the index and for within the actual calculation we evaluate the values of the nums array using the last index value subtracting that from the current I index value.
# 6. After this completes the scan of the entire array we will have found the min index.

# Analysis: So the current logic that I recently implemented in the block above that we are evaluating resulted in a runtime of 4 milliseconds and it beats 88.94% of total solutions as well as a memory of 19.15 megabytes and it beats 32.41% of solutions all together this solution resulted in the top 10% of all completed answers. 
