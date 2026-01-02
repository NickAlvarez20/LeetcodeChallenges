# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        next = None
        while curr is not None:
            next = curr.next  # Store next node
            curr.next = prev  # reverse the pointer ref (curr.next) and make it point to prev node
            prev = curr  # move prev forward | update prev node with curr node
            curr = next  # move curr forward by using ref to next || node we previously used to store curr.next (stores next node)
        return prev  # so prev at the end of the while loop points to the new head (old tail)

# Intuition: The intuition states that we need a current to point to the head of the linked list and a previous that is first set as None this stores the previous value Then we want to create a temporary variable that will store the next node in the list. We use a while loop to continue while the next reference is not None then within this while loop we use None to store a reference to the next node after that we reverse the by using the current dot next pointer and aiming it at the previous node. Then we move Prev one node forward by setting it to the current node and then we move the current node forward by setting it to our previous reference that stored the next node. At the end we return Prev since we iterated through the entire length of the linked list and at that point we are at the new head which was the old tail when we return Prev we are essentially returning the reversed linked list.
# Approach
# 1. Create three variables current which stores the head of the link list Prev which is first set as None and next which is also set as None
# 2. Initialize a while loop that continues while the current node next value is not equal to None
# 3. Update the next variable with the current.next node which stores the next node for later use
# 4. Reverse the pointer by using the current dot next pointer ref and point that now to the previous node If we are at the head this sets it to None otherwise it will point to the previous node as we move the pre node forward.
# 5. Next move Prev forward by setting it to the current node
# 6. Then move current node forward by setting it equal to our previous reference to the next node.
# 7. Finally return prevnode which will be at the end of the while loop which will be the new head The old tale per SE By returning the pre node we return the reversed linked list.

# Time complexity: O(n)
# 1. The time complexity is O of N because it is a while loop that is the main coefficient we need to evaluate for Therefore the time complexity is equal to the given length of the linked list.


# Space complexity: O(1)
# 1. The space complexity is O of one since we are doing this in place with updates to pointer references and simple iteration in moving nodes forward

# Analysis: The runtime is zero milliseconds and it beats 100 percent of submitted answers the memory is 17.94 megabytes and it beats 95.97% of solutions
# Total time to solve: At first learning this was approximately 30 minutes because I had to re evaluate and understand the animations I had to step through it sequentially with comments and understandings I would put the total time for learning at about 45 minutes.

# Alternative solutions
# 1. The recursive solution is the alternative and most common alternative It starts with a base case if head is None or next is None return the head Then it recurs until the end new head will be the last node by calling reverse list and setting new head with the self reference to head next on the way back weusehead.next.next equals the head the note after current points back to current and then we set the current nodes next becomes None then we return the original tail This uses all of in extra space The iterative version beats it on memory.
# 2. There is also the ability to use a stack Push all the nodes onto a stack and then pop them off to rebuild the list in reverse Time complexity is O of N in space is also O uses unnecessary extra space. 

