# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Init two pointers to traverse list1
        before_removal_node = list1 # Points to node just before index 
        after_removal_node = list1 # Pointers to node at index b
        
        # Move before_removal_node to the node just before index a
        # (a-1 steps forward from the head)
        for _ in range(a-1):
            before_removal_node = before_removal_node.next
        
        # Move after_removal_node to the node at index b
        # (b steps forward from the head)
        for _ in range(b):
            after_removal_node = after_removal_node.next

        # Connect the node before index a to the head of list2
        before_removal_node.next = list2

        # Traverse to the end of list2
        while before_removal_node.next:
            before_removal_node = before_removal_node.next
        
        # Connect the tail of list2 to the node after index b
        before_removal_node.next = after_removal_node.next
        after_removal_node.next = None

        return list1
        
        