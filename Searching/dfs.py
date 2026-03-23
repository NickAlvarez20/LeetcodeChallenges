# If BFS is a ripple in a pond, DFS (Depth-First Search) is like walking through a maze: you pick a path and follow it as deep as possible until you hit a dead end, then backtrack to the last fork in the road.
# In Python, DFS is most commonly implemented using recursion because the "call stack" naturally handles the backtracking for you.

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    # 1 . Mark the current node as visited
    visited.add(node)
    print(node, end=" ") # Process the node

    # 2. Visit all unvisited neighbors recursively
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    #  Using the same graph from our BFS example:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Order:")
dfs(graph, 'A')
# Output: A B D E F C 