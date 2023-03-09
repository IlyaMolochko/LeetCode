/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *node = head;
        while (node != nullptr) {
            if (node->val == 1000000) {
                return node;
            }
            node->val = 1000000;
            node = node->next;
        }
        return nullptr;
    }
};
