# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        fast = head.next
        while fast:
            node = node.next
            fast = fast.next
            if fast:
                fast = fast.next
        return node
