class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 1
        node = head
        while node.next:
            cnt += 1
            node = node.next
        if cnt == n:
            head = head.next
            return head
        else:
            cnt = cnt - n + 1
            prev = head
            node = head.next
            pos = 2
            while pos != cnt:
                prev = prev.next
                node = node.next
                pos += 1
            prev.next = node.next
            return head
