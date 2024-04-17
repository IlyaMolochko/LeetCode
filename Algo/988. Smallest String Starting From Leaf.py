# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root, path, smallest):
            if root is None:
                return
            path.append((chr(root.val + ord('a'))))
            if root.left is None and root.right is None:
                cur = ''.join(path[::-1])
                smallest[0] = min(smallest[0], cur)
            dfs(root.left, path, smallest)
            dfs(root.right, path, smallest)

            path.pop()
        
        smallest = [chr(ord('z') + 1)]
        dfs(root, [], smallest)
        return smallest[0]
