# # Intuition
# So, I see a binary tree, the root, and then I say reverse the node values at each level. We consider constraints: the root is a perfect binary tree. Once we've considered everything, we can see that depth-first search or breadth-first search would work in this given situation.

# # Approach
# So the approach is to use a Q, curr_level counter, two pointers, and a range check to process the current level.
# 1. First I want to set up an empty queue. Import DQ to make this optimized within Python. Set a current level variable to zero and check the root node for none. And then append the root to the queue.
# 2. Next I want to initialize a while queue loop so upon the queue being empty it will exit.
# 3. Then I want a conditional check if the current level modulus 2 is odd and equal to 1, we want to perform a two-pointers operation for correctly updating. So first initialize the condition to check if the current level is odd.
# 4. Next, we'll initialize left and right pointers, setting left equal to 0 and right equal to the length of q minus 1.
# 5. While left is less than right, initialize a while loop to exit when the two pointers meet.
# 6. Now, we'll simply perform a swap using the dot value notation to implement. So we use Q index access using left for the value and right for the value and we simply swap the left with the right starting at the left and right end of that current level that we are processing.
# 7. and then we increment left and decrement right for each iteration
# 8. The next part of the algorithm will first need to initialize the current length and set it equal to the length of the queue. This is going to be important for processing each level and making sure that we capture all the left and right leaves.
# 9. Initialize a for loop using i in range of the current length. This is important because for any given length of the queue, we'll want to process all the leaves, making sure they have left and right, and updating the queue accordingly for each level.
# 10. Now, within it, we can process the node. So we initialize the current node variable and set it equal to q.popleft. This will allow us to obtain the node at the current node position within the length of the queue for the current length of the queue.
# 11. Then if we see that the current node has a left leaf, we can append that to the queue and append the right leaf if it has a right leaf to the queue as well.
# 12. After we perform this, we want to make sure that we increment the level by one, so once that for loop exits, we can update the count of the level by one. That way we can check if we're on an odd or even level.
# 13. Finally, we can return the root and this will properly reverse all levels of a binary tree.


# # Complexity
# - Time complexity: O(N)
# On all levels, you look at the elements currently in the queue and swap their values. The number of elements at any level L is at most n/2 at the bottom level. Over the entire execution of the program, every note is swapped at most once. This contributes a total of O(n) work across the entire tree.
# The node processing loop, the four in range of current length loop processes every single node in the tree exactly once by popping it and pushing its children. This takes O operations. Since both phases take linear time relative to the total number of nodes, the combined time complexity is O (n), where N is the total number of nodes in the binary tree.

# - Space complexity: O(N)
# For breadth-first search, space is determined by the maximum number of nodes residing in the queue at any one time, the maximum width of the tree. The space complexity is O(n), specifically bounded by the maximum width of the tree, which is n/2 for a perfect binary tree. Because the input constraint states that it is a perfect binary tree, the last level contains exactly half of all the nodes in the tree, which is n/2. When the queue holds the entire bottom level, it uses O(n) space. Therefore, the best case and worst case space complexities for this BFS queue on a perfect tree are O(n). 

# Code

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # setup empty queue, set level to 0, check root node for None
        queue = deque()
        curr_level = 0
        if root is not None:
            queue.append(root)

        while queue:

            if curr_level % 2 == 1:
                left = 0
                right = len(queue) - 1
                while left < right:
                    queue[left].val, queue[right].val = (
                        queue[right].val,
                        queue[left].val,
                    )
                    left += 1
                    right -= 1

            curr_len = len(queue)

            for i in range(curr_len):
                # process the node
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            curr_level += 1

        return root
