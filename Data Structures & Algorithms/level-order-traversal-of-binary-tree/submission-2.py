# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        if root:
            queue.append(root)
        traversed_tree = []

        while len(queue)>0:
            level_nodes = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level_nodes.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            traversed_tree.append(level_nodes)
        
        return traversed_tree


        