# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        answ = [-1, -1]

        mn = float('inf')
        prev = head
        cur = head.next
        cur_id = 1
        prev_id = 0
        first_id = 0
        while cur.next:
            if (cur.val < prev.val and cur.val < cur.next.val) or\
               (cur.val > prev.val and cur.val > cur.next.val):
                if prev_id == 0:
                    prev_id = cur_id
                    first_id = cur_id
                else:
                    mn = min(mn, cur_id - prev_id)
                    prev_id = cur_id
            cur_id += 1
            prev = cur
            cur = cur.next
        
        if mn != float('inf'):
            answ = [mn, prev_id - first_id]
        return answ
