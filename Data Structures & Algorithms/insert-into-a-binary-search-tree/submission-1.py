# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        new_node = TreeNode(val)
        
        curr = root

        if not curr:
            return new_node
        while curr:
            if val > curr.val:
                if curr.right == None:
                    curr.right = new_node
                    break
                else:
                    curr = curr.right
            if val < curr.val:
                if curr.left == None:
                    curr.left = new_node
                    break
                else:
                    curr = curr.left
        return root
        