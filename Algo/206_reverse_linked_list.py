# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        new_head = head
        node = head.next
        new_head.next = None
        while node:
            next_node = node.next
            node.next = new_head
            new_head = node
            node = next_node
        return new_head
