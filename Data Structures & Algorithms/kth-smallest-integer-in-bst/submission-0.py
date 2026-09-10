# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_traversed_values = self.inorderTraversal(root)
        return inorder_traversed_values[k-1]

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        middle = [root.val] 
        right = self.inorderTraversal(root.right)
        return left + middle + right
    