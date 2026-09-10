"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        self.visited = {}
        return self.dfs(node)

    def dfs(self, node: 'Node') -> 'Node':
        if node in self.visited:
            return self.visited[node]

        # Clone the current node
        clone = Node(node.val)
        self.visited[node] = clone

        # Clone all neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(self.dfs(neighbor))

        return clone
        