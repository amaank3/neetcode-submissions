# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        right_view = []

        queue = deque()
        if root:
            queue.append(root)
            
        while len(queue)>0:
            level_traversal = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level_traversal.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            right_view.append(level_traversal[-1])

        return right_view