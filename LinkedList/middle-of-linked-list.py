# Intuition: For finding the middle of a linked list we can use fast and slow pointers

# Approach: 
# 1. Declare and initialize two variables slow and fast and set them equal to the head
# 2. Wow fast and fast dot next so this means while fast is not null and fast next is not null We're going to want to traverse through the linked list
# 3. As we traverse at each incremental step we want to update the slow and set it to slow dot next and then update fast and set it to fast .next.next This will allow us to create the fast and slow pointer effect that we need in order to assess the problem correctly 
# 4. After we have iterated in the conditions are no longer true we could return slow and we will be at the middle of the linked list

# Complexity:
# Time: O(n)
# Who traversed the list only once the number of operations grows linearly with the number of nodes in the list and even though the fast pointer moves twice as fast the total work is still proportional to N
# Space: O(1)
# We can use two pointer variables slow and fast regardless of how large the linked list is So this is going to be constant space we have no extra structures no arrays hash maps to store the nodes this method does not require additional memory that scales with input size .


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
