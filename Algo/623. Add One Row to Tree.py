# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val, root)
            return new_root
        
        q = deque()
        q.append(root)
        cnt = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                top = q.popleft()
                tmp = None
                if top.left:
                    tmp = top.left
                    q.append(tmp)
                if cnt == depth -1:
                    top.left = TreeNode(val, tmp)
                tmp = None
                if top.right:
                    tmp = top.right
                    q.append(tmp)
                if cnt == depth -1:
                    top.right = TreeNode(val, right=tmp)
            cnt += 1
        return root
