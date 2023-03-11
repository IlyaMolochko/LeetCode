/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> v;
        ListNode *node = head;
        while (node != nullptr){
            v.push_back(node->val);
            node = node->next;
        }
        return build(v.begin(), v.end());
    }
    
    TreeNode* build(vector<int>::iterator b, vector<int>::iterator e){
        TreeNode *node = nullptr;
        if (e - b > 1){
            vector<int>::iterator m = b + (e - b) / 2;
            node = new TreeNode(*m);

            node->left = build(b, m);
            node->right = build(m + 1, e);
        } else if (e - b == 1){
            node = new TreeNode(*b);
        }
        return node;
    }
};
