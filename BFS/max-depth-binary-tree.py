# # Intuition
# To calculate the maximum depth, we can use breadth-first search or DFS.

# # Approach
# 1. from collections import DQ
# 2. Then we want to set up an empty queue so set queue variable equal to DQ. Create a max depth variable, set it equal to zero. This will be important as we go through the levels of the tree to increment.
# 3. Guard clause up front checks if the root is not None. We can append the root to the queue; else we can immediately return zero.
# 4. While the queue is not empty, Calculate the depth so we're going to initialize a queue and use a while loop.
# 5. Create a variable called levelSize set it equal to the length of the current queue. This will allow us to properly iterate through each level of the queue at its current size to check left and right children.
# 6. Now set up a for loop for the range of the level size.
# 7. Create a variable called currentNode which will process the currentNode and pop left off of the queue.
# 8. Using the current node we can check if it has a left child, if so we can append that to the queue and then we can check for the right child as well.
# 9. Once we have completed this process for that entire level, we can increment the max depth by one, thus allowing us to know when we are shifting after we have processed the current level.
# 10. We can finally return the max depth and we will have properly solved.

# # Complexity
# - Time complexity: O(N)
# We visit every node in the binary tree exactly once. For each node popping from the deque and pushing its children takes constant time. Therefore the time complexity is O(N) where N is the total number of nodes in the tree.

# - Space complexity: O(N)
# The auxiliary space is determined by the maximum size of the queue. In a BFS search, the queue holds at most one level of nodes at any given time. In the worst case, a fully balanced binary tree, the lowest level contains around n divided by 2 nodes, which yields a space complexity of O(n).

# Code

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        max_depth = 0

        if root is not None:
            queue.append(root)
        else:
            return 0

        # calculate the depth
        while queue:
            level_size = len(queue)

            for i in range(level_size):
                curr_node = queue.popleft()

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            max_depth += 1
        return max_depth
