class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

# Intuition:
# So we use two pointers left and right to traverse through increasing the left pointer and decreasing the right pointer if we do not have the target sum matching and then after we find the correct target we match by Assigning to the list the left and right pointer which will be the index of the left and right pointer. This will properly solve the problem using the 2 pointers techniques.
#
# Approach:
# 1. So first we want to assign left and right left to zero index and length of numbers minus 1 for the right pointer
# 2. Then initialize a while loop while left pointer is left in the right This will indicate the exit condition
# 3. If left value plus the right value of where the left index and right index are currently at equals the target we return the left pointer 1 and the right pointer 1 within a list for one based index as the question has asked for. It's good to note that if you do not include the plus one it will return the incorrect answer. 
# 3. Else if numbers left plus numbers right is left in the target then we increment the left counter
# 4. Else we just decrement the right counter and perform the loop checking the condition.
# 5. In this question you return as soon as the if indicates which shows control flow early exit so you don't have to initiate through the entire process which it will exit early rather than having to go through the entire logic block this is also good practice. 


# Time complexity: O(n)
# We iterate through the numbers list and we compare which is constant operations O of one time and the while loop itself is the biggest coefficient in this situation which results in O(n) Time complexity
# Space complexity: O(1)
# The space complexity is out of one since we are using two pointers to scan within place and there are no separate data structures being added for additional memory it uses one block of memory which is the numbers list and the left and right variables. This is directly in line with the requirement that the solution must only use constant extra space. 

# Analysis:
# This current solution has a 7 millisecond runtime it beats 26.8% of solutions and a memory of 20.63 megabytes it beats 16.47% this places the solution in the top 50% of all solutions.
# The total time to solve this medium level problem was one minute.


# Alternative approaches:
# 1. I could use a hash map dictionary approach iterate through the array wants for each number check if it's complement target minus number exists in a dictionary This is the gold standard for the uncertain version of this problem it uses OVA in extra space to store the hash map which violates the constant extra space constraint often required for the sorted version complexity of time is oven and space is oven with the hash map approach. 
# 2. I could use a binary search approach for each number X in the input array perform a binary search for the value target minus X in the remaining part of the array maintains O-1 space and is faster than a nested loop slower than two pointers because it performs log in Word for every element complexity is in log N time and O constant space
# 3. You could do a brute force with nested loops use two nested loops to check every possible pair in the array simple to implement extremely inefficient which is a time complexity of O(N^2)  and O(1) space
