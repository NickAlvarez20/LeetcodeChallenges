# Topological Sort is a bit different from the others because it doesn't work on lists of numbers—it works on Directed Acyclic Graphs (DAGs).
# Think of it like a project task list: you can't put on your socks until you've put on your underwear, and you can't put on your shoes until you've put on your socks. Topological sort gives you the linear order to complete these tasks.

# (Kahn's Algorithm)
# This is the most common approach because it uses a simple Queue and tracks the "in-degree" (how many prerequisites a task has).

from collections import deque


def topological_sort(num_nodes, edges):
    # 1. Represent the graph and track in-degrees
    adj = {i: [] for i in range(num_nodes)}
    in_degree = {i: 0 for i in range(num_nodes)}

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    # 2. Add all nodes with 0 prerequisites (in-degree 0) to the queue
    queue = deque([i for i in in_degree if in_degree[i] == 0])
    topo_order = []

    # 3. Process the queue
    while queue:
        u = queue.popleft()
        topo_order.append(u)

        # For every neighbor, "complete" the prerequisite
        for v in adj[u]:
            in_degree[v] -= 1
            # If all prerequisites are met, add to queue
            if in_degree[v] == 0:
                queue.append(v)

    # 4. Check for cycles (if topo_order doesn't include all nodes)
    if len(topo_order) != num_nodes:
        return "Cycle detected! Topological sort impossible."

    return topo_order


# Example usage (0: Underwear, 1: Socks, 2: Shoes, 3: Pants)
# 0 -> 3 (Underwear before Pants)
# 1 -> 2 (Socks before Shoes)
# 3 -> 2 (Pants before Shoes)
tasks = 4
dependencies = [(0, 3), (1, 2), (3, 2)]

print(f"Task Order: {topological_sort(tasks, dependencies)}")
