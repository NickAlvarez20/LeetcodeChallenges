# Intuition: The main theme that jumps out for this one is iterating and knowing how to iterate through a linked list and move and update the current position as well as iterating to the entire end of the link list another important concept is string building and then converting to an integer with a comma inside of the argument box and then putting a 2

# Approach:
# 1. Want to uncomment the initialization so we can get the link list class working correctly we're going to need access to the valve 
# 2. W Declare a result variable and set it equal to an empty string Declare a current variable and set it equal to head 
# 3. Initialize a while loop that says while current exists then
# 4. We're going to build out result plus equals and we're going to want to convert it into a string before sending it over to result so we don't have a mismatch in data types and within arguments and parameters we're going to set it equal to current dot value We want to access the value
# 5. We're going to update for each part of the iteration as long as current is a condition that exists we're going to increment it for each step current dot next
# 6. At the end of the loop we are going to Convert the result into a base two integer instead of the default base 10 and return the result and we will have successfully solved the problem


# Complexity:
# Time: O(n)
# Who traversed the list only once the number of operations grows linearly with the number of nodes in the list and even though the fast pointer moves twice as fast the total work is still proportional to N
# Space: O(1)
# We can use two pointer variables slow and fast regardless of how large the linked list is So this is going to be constant space we have no extra structures no arrays hash maps to store the nodes this method does not require additional memory that scales with input size .


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = ""
        current = head
        while current:
            result += str(current.val)
            current = current.next
        return int(result, 2)
