# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        prevEncount = []
        while curr is not None:
            prevEncount.append(curr)
            curr = curr.next
            if curr in prevEncount:
                return True
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()
        while curr is not None:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False


# Intuition: Traverse the linked list and use a previously encountered set to determine if we have already seen that node Traverse the linked list and for each part we want to see if current is in the previously encountered list if it is then we can say return true else we return false.
# Approach
# 1. Create a variable and store the head of the node for traversal
# 2. Create a previously encountered list and initialize it as empty
# 3. Implement a while loop that checks while current is not None which means that the node has a value and a pointer
# 4. For each iteration we want to append the current node into the previously encountered
# 5. Then we want to increment current to the next node
# 6. Then we want to check if current node has been seen in previously encountered we return true
# 7. Finally we return false if we are on the current next node and it has not been seen and we reach the end None which means that we have not previously encountered so we return false

# Time complexity: O(n)
# 1. The time complexity given the largest coefficient is the while loop therefore the time complexity is ON for the given length of the linked list


# Space complexity: O(N)
# 1. The space complexity is O of N since we are building a previously encountered with this solution

# Analysis: The runtime for this solution is 854 milliseconds which is suboptimal and only beats 6% of total solutions therefore it is in the lower 95% The memory is 95.39% with 19.25 megabytes which beats 95% of all other answers
# Total time to solve: Total time to solve was only five minutes Due to previous exercises of linked list the pattern was pretty straightforward Simple while loop variables incrementation and then checking at each step if we have previously encountered the current next node

# Alternative solutions
# 1. Alternative solution would be to check maybe using two pointers is what I would assume here One to keep track of the current variable and the second one that continues to move throughout the entire linked list and if the variables match then we return true I believe that would be the O of 1 space time complexity.
# 2. We may also be able to implement a stack although this would be less suboptimal.
# 3. We may be able to implement a similar solution using Set instead of List
