# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = set()
        nodes = []
        node = head
        s = 0
        st.add(s)
        while node:
            s += node.val
            if s in st:
                while nodes and nodes[-1][1] != s:
                    st.remove(nodes[-1][1])
                    nodes.pop()
                if nodes:
                    nodes[-1][0].next = node.next
            else:
                nodes.append([node, s])
                st.add(s)
            node = node.next
        return None if not nodes else nodes[0][0]
