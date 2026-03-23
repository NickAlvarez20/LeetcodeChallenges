# Breadth-First Search (BFS) is a "layer-by-layer" search. Imagine dropping a pebble in a pond: the ripples expand outward in circles, hitting all the closest points before moving further out.
# In code, BFS is almost always implemented using a Queue (First-In, First-Out) to keep track of which nodes to visit next.
# YouTube
# YouTube
# Python Implementation
# We use a dictionary to represent the graph and collections.deque for an efficient queue.
# GeeksforGeeks
# GeeksforGeeks
#  +2

from collections import deque

def bfs(graph, start_node):
    # 1. init: Add start node to queue and mark it visited
    visited = {start_node}
    queue = deque([start_node])

    while queue:
        # 2. Dequeue: Take the first node added to the queue
        current = queue.popleft()
        print(current, end=" ") # Process the node (e.g., print it)

        # 3. Explore Neighbors:
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Example Graph (Adjacency List)
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("BFS Order:")
bfs(graph, "A")
# Output: A B C D E F
