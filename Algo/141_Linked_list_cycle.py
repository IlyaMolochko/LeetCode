# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        if not head or not head.next:
            return False
        fast = head.next
        while node and fast:
            if fast == node:
                return True
            node = node.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
        return True
