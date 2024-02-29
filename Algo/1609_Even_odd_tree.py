# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        level = 0
        answ = True
        while q and answ:
            size_of_queue = len(q)
            prev = None
            for _ in range(size_of_queue):
                node = q.popleft()
                if node.val % 2 == level % 2:
                    answ = False
                    break
                if prev is None:
                    prev = node
                elif level % 2 == 0 and node.val <= prev.val or \
                     level % 2 == 1 and node.val >= prev.val:
                    answ = False
                    break
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node
            level += 1
        return answ
