# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], s: int) -> int:
            if root.left is None and root.right is None:
                return 10 * s + root.val
            res = 0
            if root.left:
                res += dfs(root.left, 10 * s + root.val)
            if root.right:
                res += dfs(root.right, 10 * s + root.val)
            return res
        return dfs(root, 0)
