class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left] , s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


# Intuition:
# So the idea is to iterate through the entire length of the array and swap in place so we use two pointers.
#
# Approach:
# 1. Assign left and right pointers set left equal to zero and right equal to the length of the array minus 1(Minus 1 because computer indexes are zero based therefore we need to subtract by one to not iterate outside the length of the array)
# 2. we create a while loop while the left pointer is less than the right
# 3. We swap the left character with the right character by using array based index using left and right to access the indexes at the current position
# 4. And then we increment the left by one
# 5. Then we decrement the right by one
# 6. Finally we return the array or the string and that will have the proper reverse.

# Time complexity: O(n)
# The time complexity is O(n) since we have to iterate through the entire length of any given string. It's also important to note that with the left and the right we actually only iterate through half of the string (n/2) iterations. The swap Using simultaneous assignment is O(1) operation time.
# Space complexity: O(1)
# The base complexity since we are swapping in place is constant declaring a variable and swapping are all constant time.


# Analysis:
# The runtime is zero milliseconds it beats 100% of solutions and the memory is 23.49 megabytes it beats 33.9% of solutions and this helps us learn two pointers. Solved in 20 seconds. 
# Alternative Solutions
# 1. Reverse in place with Python reverse method
# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         return s.reverse()

# 2. In place list reversal via slice assignment
# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         s[:] = s[::-1]


# 3. Recursive approach - slowest runtime, high memory usage  
# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         # Define a helper function to handle the indices
#         def helper(left: int, right: int):
#             # Base case: when pointers meet or cross, stop
#             if left >= right:
#                 return

#             # Action: Swap the characters
#             s[left], s[right] = s[right], s[left]

#             # Recursive step: Move pointers inward
#             helper(left + 1, right - 1)

#         # Kick off the recursion with the initial boundaries
#         helper(0, len(s) - 1)
