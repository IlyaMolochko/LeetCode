# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], is_left: bool=False) -> int:
            s = 0
            if not root.left and not root.right and is_left:
                return root.val
            if root.left:
                s += dfs(root.left, True)
            if root.right:
                s += dfs(root.right)
            return s
        
        return dfs(root)
