# # Intuition
# I see a tree. I immediately start thinking about using BFS/DFS for traversal and proper data operations.

# # Approach
# 1. So we need to have a class for the tree node, self.val, self.left, self.right. We can initialize val with a default condition of 0, left with a default condition of None, right with a default condition of None. And also ensure we have self passed into the __init__ constructor as the first parameter.
# 2. Then we can define the class for the solution and write a function within it, aka a method called invertTree, within the parameters we pass self, root as an optional tree node, which returns an optional tree node. For this problem, we need to return the root, so this is the best way to set up the original function.
# 3. Next we want to import from collections DQ. Use that to create a variable called Q and declare it as a DQ that is empty. This will give us access to DQ for optimal time and space complexity optimizations.
# 4. Then we want to check if the root is not None because if it is, that will have an edge case error. Therefore, we will check with a conditional guard clause: if root is not None, then we're going to append the very start of the tree root to the queue.
# 5. We start and initialize a while QisNotEmpty loop.
# 6. We want to declare a current variable set that equal to the current node by popping left from the queue, which will allow us to start with the root node for traversal. So, we set cur equal to the root node.
# 7. Then we want to swap the left and the right nodes since we are inverting the binary tree. This is the first part of the operation. So we use Python's swap mechanism and simply assign.
# 8. Then we want to check for the children of the left. If current.leftChild exists, we want to append to the queue the current child of the left node of any given node as we traverse. We also want to make sure that we're adding the right child, so vice versa, perform the same operations for the left and the right.
# 9. Then we want to return the root at the very end and this will allow us to return the node root of the tree verifying that we have met the test requirements and have passed the solution successfully inverting the tree.

# # Complexity
# - Time complexity: O(N)
# In the worst-case situation, we'll have to go to the base of the tree, so the time complexity is O(n) in the worst-case situation. Otherwise, it is O(n) divided by 2, but since this is an inversion, we're always going to need to go to the very end to check everything and reverse and invert it, so therefore it's O(n).

# - Space complexity: O(N)
# As we build out the queue, we are popping all of the nodes from the tree, reversing the operation, swapping, and then accounting and adding to the queue. So this is going to span until the entire length of the tree, resulting in O of N auxiliary space. In reality, BFSQs never hold the whole tree at the same time, so the queue only holds one level of the tree at a time. In a perfectly balanced binary tree, the bottom level leaf level contains roughly N divided by two nodes, half the entire tree. Therefore, at its maximum size, the queue will hold N divided by two nodes. Since we drop constants in big O, N divided by two simplifies to N. Note that if the tree is just one long straight line, a degenerate tree like a linked list, the queue only ever holds one node at a time, making the space O of 1 in the specific best case scenario.

# # Code

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque()

        if root is not None:
            queue.append(root)

        while queue:
            curr = queue.popleft() # assign curr node to curr
            curr.left, curr.right = curr.right, curr.left #swap left and right nodes

            # check for children of left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root
