class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(0, len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                if (
                    i != left
                    and i != right
                    and left != right
                    and nums[i] + nums[left] + nums[right] == 0
                ):
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
        return result


# Intuition:
# The first part of the intuition is to recognize that we will need 2 pointers and a for loop with a while loop The for is identified when the keyword duplicate is mentioned. Another key part is having two checks for two of the pointers the left and the left plus one pointer specifically we need conditional checks to identify if they equal the previous value before them if they do we have to continue and then this will reach the second part of the logic where the left pointer is equal to And when that is the situation we increment the left Pointer buy one until this condition no longer exists. So on the first pass we can use that as a pair but any subsequent passes that have identical values the for loop will correctly implement this logic first continuing and then stepping into the other condition that will increment the left pointer until these I index value and left pointer value no longer Equal Also known as they are no longer a match. So we'll need two pointers and a for loop some people may think of this as a 3 pointer technique with I as the 3rd pointer.
#
# Approach:
# 1. So we must create a results that we're going to append the pairs to
# 2. Then I sort the array. this is a key part of the process because when we increment the counters left and decrement right we will need to understand the order of the values in order to increment and decrement properly
# 3. Then create a for loop for I in range of zero to length of nums one. The alternative approach is to iterate until the length of the nums array minus 2 and this is Logical because our left pointer will reach the right pointer sooner than a traditional approach of two pointers.
# 3. Then a very important key part of the process happens we check if I is greater than zero and the value is equal to the value before it then we continue this will allow us to step into the ....e increment the left pointer plus one
# 4. Then we assign left and right left will be Assigned as I plus one and right will be the length of nums minus one
# 5. Then we initialize the while loop with the conditions left less than right.
# 6. We have a initial conditional check if I does not equal left and I does not equal right and left does not equal right and the values of I left and right at their current positions equal zero
# 6a. Then we're going to append those values into our result
# 6b. Increment left plus one
# 6c. Decrement right minus one
# 6d. And then a key component of logic takes place we initialize another while loop and this one states while left pointer is less than right pointer and the current value at nums left equals NUM's left minus one This means we have duplicates up until that left pointer. On the initial pass this was OK but any subsequent pass we need to keep incrementing the left pointer until we no longer have the same value As the previous position.
# 6d(a). Then I increment the left pointer plus one
# 7. Then we want to check if the current triplet sums to less than zero
# 7a. Then we increment the left pointer by one
# 8. Then check if the current triplet sums to greater than zero
# 8a. If it does then we decrement the right pointer by one
# 9. Finally we can return the result which has the result and result stores all non duplicate triplet pairs that exist within the nums array that add to zero.


# Time complexity: O(n^2)
# Sorting takes (nlogn)time
# Nested loops the outer loop runs in time and for each iteration the left and right pointers traverse the remainder of the list once ON this results of O(n^2)
# Space complexity: O(1) to O(n)
# In Python the sort method tim sort requires ON auxiliary space in the worst case
# Excluding the space required for the output list a two pointer logic itself uses O-1 additional space.

# Analysis:
# The runtime was 1226 milliseconds it beats 12.51% of all solutions and the memory is 22.45 megabytes and it beats 14.95% of solutions altogether the combination of these two places within the top 75 per cent of all answers.


# Alternative approaches:
# 1. You could use a hash set or a hash map with no sort you can solve the problem without sorting by using a hash set to find the complement So we fixed two elements A and B then check if minus A plus B exists in a hash map to avoid duplicate triples without sorting you must store the triplets in a sorted tuple set complexity is of N ^2 time and O of N space to store all elements in the hash set
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         res, dups = set(), set()
#         seen = {}
#         for i, val1 in enumerate(nums):
#             # Skip the first element if we have already processed it as a pivot
#             if val1 not in dups:
#                 dups.add(val1)
#                 for j, val2 in enumerate(nums[i + 1 :]):
#                     complement = -val1 - val2
#                     # If complement exists and was seen in this specific i-loop
#                     if complement in seen and seen[complement] == i:
#                         # Sorting the triplet ensures unique entry in the 'res' set
#                         res.add(tuple(sorted((val1, val2, complement))))
#                     seen[val2] = i
#         return [list(x) for x in res]


# 2. We could do bit sets and FFT for small ranges if the numbers are within a small range negative U to U you can treat the input as a polynomial and use a fast Fourier transform Represent the input as a big vector polynomial squaring the polynomial effectively computes all pair Y sums via discrete convolution Complexity is all of U log U time where U is the range of the integers
# 3. You could also do a sub quadratic research algorithm theoretically threesome can be solved slightly faster than O of N squared on modern hardware The logic is to use techniques like bit packing or complex decision trees Researchers have found algorithms that run in roughly O of N ^2 divided by log N ^2 time. Note these are highly complex and generally not practical for standard interview settings or typical software development. Key take away is the hash set approach is great if you aren't allowed to modify sort the original array but it requires more memory than this current 2 pointer solution.
