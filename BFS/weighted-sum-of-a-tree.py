# # Intuition
# The problem provides a parent array representing a tree structure where each node has an associated value in numbers. The weight of each node depends on its depth relative to the maximum height of the tree. My first thought was to calculate the weighted sum. I need to know two crucial pieces of information for every node: its individual depth and the maximum height of the entire tree. The height list starting from the root node at 0. Since finding the shortest distance or depth level by level from a root node is a textbook application of the breadth-first search. Utilizing a key allows me to naturally map out every node's depth. Once the maximum height is determined from these depths, I can calculate each node's inverse weight and accumulate the final total.

# # Approach
# 1. Graph reconstruction requires building an adjacency list from the parent array to map parents to child nodes, establishing directed edges downward from the root.
# 2. So first we have to create an empty dictionary.
# 3. Now to populate the adjacency list, first, I want to say for i in range length of parent we're going to use this as the initial setup implementation for the loop and then within this we want to add to the adjacency list using i as the key and passing an empty array.
# 4. Next I want to populate the in array the associated value for each level.
# 5. So I use indexValue in enumerating the parent array and if the value does not equal 1 then we can assign the adjacencyList key and append it with the index. So for each value that we're passing into it we'll have the value and then we'll have all the indexes that are associated with that. So for example, if we're on index or value 0 and we see a bunch of others that have the 0, we can now append the indexes that belong to that 0.
# 6. Now we want to start the queue to find the depths using a breadth-first search.
# 7. So we'll use the deque from collections import deque and then we want to initialize the queue with node 0 and root 1 using a tuple within an array in order to set this up properly because of the adjacency list formatting.
# 8. Now, node_depth, so we're going to set that equal to an empty dictionary. We're going to store each node depth for calculations later.
# 9. Now we're going to use BFS to traverse and we're going to initialize a queue with a condition for iteration.
# 10. We're gonna unpack the tuple using syntax curlow curlow is equal to q.pop left. This will allow us to unpack each current node within the queue.
# 11. Next we're going to use node depths, passing the current node as the key and setting the value assigned to that dictionary equal to the current depth. We'll create a hash map with this sequence, thus assigning the correct depths that will be used for access later during the equational part of the algorithm.
# 12. Now we're going to go for the leaf in the adjacency list passing the currentNode as the key. We're going to append using a tuple of the currentLeaf as well as the currentDepth plus one. So we're going to assign the node and the current depth that that node is at. We'll use this tuple for later, but we're essentially populating the queue.
# 13. Now we're going to use height and set that equal to the max of the node depth and use dot notation to grab the values from the node depth hash map and then that will identify the maximum height.
# 14. We're going to set total weight equal to zero., Declaring a variable called totalWeight for the final part of the process, determining the total weight of the weighted sum of a tree.
# 15. Now we're going to initialize a for loop for eye and range of length of parent.
# 16. Declare a variable called d and using the node depth hash map we can pass i to it and this will give us the current depth that has been assigned in the hash map using i as the key to access the associated value.
# 17. We can create a weight variable, set it equal to the current value of nums, passing I times height minus D, plus 1, which is the equation that we were originally given.
# 18. Now for total weight we can add the weight that was determined by the previous variable that was assigned to total weight.
# 19. Finally, we can return the total weight and this will have the weighted sum of a tree.

# # Complexity
# - Time complexity: O(N)
# Graph construction iterating over the parent array to build the adjacency list takes O(n) time. The breadth first traversal, the while loop visits every node exactly once and looks at each edge once which takes O(n) time. The max height and total calculation for finding the max value in node depth takes O(n) time. And the final for loop running through the nodes take another O(n) time. Combining these consecutive steps yields a purely linear time complexity of O(n) time where n is the number of elements in the parent list.

# - Space complexity: O(N)
# The adjacency list storing the graph structure takes O(n) space for the keys and child arrays. The node-depth map, the node-depth dictionary stores exactly in key-value pairs which takes O(n) space. The breadth-first search queue in the worst-case scenario, such as a perfectly balanced tree or a star-shaped tree graph, the queue will hold up to the maximum width of the tree which is bounded by O(n). The total space since all of our data structures scale nearly with the size of the input, the overall auxiliary space complexity is O(n).

# Code

from collections import deque

class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:

        adjacency_list = {}

        for i in range(len(parent)):
            adjacency_list[i] = []

        for index, val in enumerate(parent):
            if val != -1:
                adjacency_list[val].append(index)

        # start queue to find depths using BFS
        queue = deque([(0,1)]) # node 0 and root 1
        node_depths = {} # store each nodes depths for calculations later

        while queue:
            curr_node, curr_depth = queue.popleft()
            node_depths[curr_node] = curr_depth 

            for leaf in adjacency_list[curr_node]:
                queue.append((leaf, curr_depth+1))

        height = max(node_depths.values())
        total_weight = 0
        for i in range(len(parent)):
            d = node_depths[i]
            weight = nums[i] * (height-d +1)
            total_weight += weight
        return total_weight
