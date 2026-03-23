# To learn graphs and union find, focus on mastering the mindset of representing connections (nodes and edges) and efficiently managing groups of related items. While graphs model the overall structure, Union-Find is a specialized tool used to track "who belongs to which group" in constant time. 

# 1. Core Concepts and when to use
# - Connectivity: You need to find if point A can reach point B (e.g., is there a path?)
# - Relationship Mapping: Data in linked together, like friends in a social network or cities on a map.
# Interview clues - Looks for keywords like "connected components", "cycles", "redundant connections", or "shortest path". If you need to merge groups frequently, Union-Find is the intended path. 

# Most graph problems fall into BFS, DFS, Union-Find(DSU), Topological sort. 
# BFS - Explore level by level using a queue. best for shortest paths
# DFS - Explore as deep as possible using Recursion, best for visiting every node.
# DSU - Use a "parent" array to merge sets and find group leaders.
# Topological sort - Order nodes based on dependencies (A must happen before B or prerequisites)

# The Disjoint Set Union  (DSU) is a simple class that lets you Union (join two groups) and Find (see which group a node belongs to)

class UnionFind: 
    def __init__(self, n):
        # Each node is initially its own parents (its own group leader)
        self.parent = list(range(n))

    def find(self, i):
        # Recursively find the "ultimate leader" of the group
        if self.parent[i] == i:
            return i
        # Path Compression: Point directly to the leader to speed up future lookups
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
        # Join the two groups by making one leader the parent of the other
            self.parent[root_i] == root_j
            return True # Successfully merged
        return False