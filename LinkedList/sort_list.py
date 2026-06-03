class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: 0 or 1 nodes are already sorted
        if not head or not head.next:
            return head
        
        # Part 1: Find the middle to split the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None # Break the link

        # Part 2: Recursively sort
        left = self.sortList(head)
        right = self.sortList(mid)

        # Part 3: CALL the merge function to join them
        return self.merge(left, right)

    # Make sure this is indented inside the Solution class
    def merge(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Attach whatever remains of either list
        curr.next = list1 or list2
        return dummy.next
