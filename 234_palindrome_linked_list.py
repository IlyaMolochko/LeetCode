# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cnt = 0
        node = head
        while node:
            cnt += 1
            node = node.next
        pos = 1
        node = head
        prev = None
        while pos <= cnt // 2:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
            pos += 1
        if cnt % 2 == 1:
            node = node.next
        while node and node.val == prev.val:
            node = node.next
            prev = prev.next
        return node is None
