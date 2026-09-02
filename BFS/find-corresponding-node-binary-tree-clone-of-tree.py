# # Intuition
# So for this problem we are going to use breadth first search in order to traverse through the tree and look at the current position within the original tree and then return the current position within the clone tree.

# # Approach
# 1. So first we want to make sure that we have set up the tree node it's given for this problem but honestly we need to create a class called tree node define using init for self and x set self.value equal to x self.left equal to none self.right equal to none.
# 2. Then we want to initialize the class of solution and define get target with self original tree node clone tree node target Set the tree node and then it returns a tree node
# 3. Note that parts 1 and 2 are not expected, but it's good knowledge to note in general when setting up a breadth-first search to initialize the nodes as well as initialize the getTargetCopy function analyzer.
# 4. So, we're going to initialize the original tree queue and clone tree queue. Set them equal to empty stacks. Those will be two variables that we first initialize upon starting the solution.
# 5. Once we have the queue set up, we go into the root of the original and cloned.
# 6. Then we can start the while loop with the condition for exit being that the original tree queue is empty.
# 7. We want to declare two variables within the while loop, current original and current clone. We're going to pop off of the queues the first element within each and store them within these variables. This way we can use them for later data analysis.
# 8. We want to set a conditional check for exit. We can do this at the start before going deeper into the algorithm for ultimate efficiency. If the current original is equal to the target, so the node is equal to the target node, tree node, we can return the position within the current clone, which will also give us the relevant node that we are ultimately looking for.
# 9. Next, we can continue with the traversal if we do not find the node that is equal to the target. Then, we're going to set a condition. If the current original node's left exists, we want to append the original tree queue with the current original left child, and then append to the queue for the clone tree the current clone left child.
# 10. Then we want to look at if currentOriginal.write exists for the writeChild node. We can dive into this, making sure that it's not equal to none, and then append to the original tree and clone tree the writeChild and the writeChild of the clone. This will allow us to complete the BFS traversal properly.

# # Complexity
# - Time complexity: O(N)
# The worst-case scenario if the target node is at the very last leaf of the tree or not in the tree at all, the loop will visit every single node exactly once. The hidden Python catch to use py0 on a standard Python list.

# Python popping from the front of a standard list requires shifting all other elements over, taking O(n) time where n is the current size of the queue. For a perfect BFS, we can use a deque and pop from the left.

# - Space complexity: o(N)
# Queue size in BFS for a perfectly balanced binary tree, the queue holds the nodes at the current level. The bottom widest leaf level contains roughly half the number of nodes.
# Because your questions hold up to half the node at its widest point, the space complexity is proportional to N.

# Code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        original_tree_queue = []
        cloned_tree_queue = []

        original_tree_queue.append(original)
        cloned_tree_queue.append(cloned)

        while original_tree_queue:
            curr_orig = original_tree_queue.pop(0)
            curr_clone = cloned_tree_queue.pop(0)
            if curr_orig == target:
                return curr_clone
            
            if curr_orig.left:
                original_tree_queue.append(curr_orig.left)
                cloned_tree_queue.append(curr_clone.left)
            if curr_orig.right:
                original_tree_queue.append(curr_orig.right)
                cloned_tree_queue.append(curr_clone.right)
