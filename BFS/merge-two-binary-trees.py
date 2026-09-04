# # Intuition
# So merging two binary trees will most likely require a breadth-first search and depth-first search. So it looks like we are supposed to return the merge tree and the merge rules that if two nodes overlap then some node values are updated. So in order to check level by level if a node exists within each tree the most likely solution would be breadth-first search. Although depth-first search can work.

# # Approach
# 1. If the root1 doesn't exist, return 2 immediately. If root2 doesn't exist, return root1 immediately. Essentially, this allows us to stop the entire algorithm if neither tree exists.
# 2. Now we want to create a queue and we're going to use this queue for both tree's root1 and root2. So using from collections, we can import deque for the optimal time complexity and efficiencies.
# 3. Now we can check if roots are not None before sending roots to q. So if root1 is not None and root2 is not None, tree1q append within a tuple root1 and root2. It's important to use the pairs tuple for this because that will allow us to merge precisely and correctly.
# 4. Now, while Tree1Q, this is the exit condition, so as long as the queue exists, we're going to continue the while loop.
# 5. First part of the process within the while loop is to unpack the tuple so we set cur_node1 and cur_node2 equal to tree1_q.popleft() which will pop off the tuple and allow us to unpack and store within the variables cur_node1 and cur_node2 which we will use later for processing.
# 6. For each iteration, we want to update the currentNodeVal for 1. If basically we're saying curNode1 exists and curNode2 exists, then we're going to merge these values otherwise this condition will not operate and execute. Therefore, we can set up this for each iteration curNode1.value equals curNode1.value plus current node 2 dot value.
# 7. Now, if we're checking the left node for career node 1 and career node 2, and we see the left leaf exists for both of these, then we can append the left and the tree to left leaf to the queue.
# 8. Else if currentNode2.left exists and there's not a left leaf on tree1 then we can simply move the entire left child node to the position within the current node within tree1 thus successfully merging the left child at that position.
# 9. Now we repeat this process. We check if right for tree1 and tree2 exist within the leaves. If so, we can append them to the queue. And we don't have to explicitly check for the tree1 right leaf because we can simply pass by that condition and it will successfully merge the tree. Otherwise, we're going to check. If the right tree has a right leaf, then we can update within tree1 all the values that are assigned to that right child.
# 10. Then we can return root1 and that will successfully merge the trees


# # Complexity
# - Time complexity: O(min(N,M))
# Time complexity is linear time relative to the number of overlapping nodes. So it's O where N and M are the total number of nodes in tree 1 and tree 2 respectively. The algorithm only traverses the nodes that overlap between both trees. The moment a node exists in one tree, the algorithm graphs that entire subtree in O of one time and skips traversing it, strictly bounded by the size of the smaller tree's overlapping structure.

# - Space complexity: O(min(N,M))
# Space complexity is also OminN,M or NNM are the total number of nodes in tree1 and tree2 respectively. The space is determined by the maximum number of node pairs stored in the queue at any given time. For a completely full binary tree, the maximum width of the tree occurs at the leaf level which contains roughly half of the total nodes. Since we only queue overlapping nodes, the maximum size of the queue is proportional to the width of the shared overlapping structure. Bounding it to O(min(N,M)).

# Code

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        # create a queue
        tree_1_queue = deque()

        # check if roots are not none before sending roots to queue
        if root1 is not None and root2 is not None:
            tree_1_queue.append((root1, root2))
        

        while tree_1_queue:
            curr_node_1, curr_node_2 = tree_1_queue.popleft()
            curr_node_1.val = curr_node_1.val + curr_node_2.val
            if curr_node_1.left and curr_node_2.left:
                tree_1_queue.append((curr_node_1.left, curr_node_2.left))
            elif curr_node_2.left and not curr_node_1.left:
                curr_node_1.left = curr_node_2.left
            if curr_node_1.right and curr_node_2.right:
                tree_1_queue.append((curr_node_1.right, curr_node_2.right))
            elif curr_node_2.right and not curr_node_1.right:
                curr_node_1.right = curr_node_2.right
            


            

        return root1


# curr_val = 0
#             if curr_node_1 and curr_node_2:
#                 curr_val += curr_node_1.val + curr_node_2.val
#                 if curr_node_1.left:
#                     tree_1_queue.append(curr_node_1.left)
#                 if curr_node_1.right:
#                     tree_1_queue.append(curr_node_1.right)
#                 if curr_node_2.left:
#                     tree_2_queue.append(curr_node_2.left)
#                 if curr_node_2.right:
#                     tree_2_queue.append(curr_node_2.right)
#                 result.append(curr_val)
#             elif curr_node_1 and not curr_node_2:
#                 if curr_node_1.left:
#                     tree_1_queue.append(curr_node_1.left)
#                 if curr_node_1.right:
#                     tree_1_queue.append(curr_node_1.right)
#                 result.append(curr_node_1.val)
#             elif curr_node_2 and not curr_node_1:
#                 if curr_node_2.left:
#                     tree_2_queue.append(curr_node_2.left)
#                 if curr_node_2.right:
#                     tree_2_queue.append(curr_node_2.right)
#                 result.append(curr_node_2.val)
