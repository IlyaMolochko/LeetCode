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

struct st{
    TreeNode *node;
    int d;
};
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        queue<st> q;
        q.push({root, 1});
        int answ = 0;
        while (!q.empty()) {
            auto top = q.front();
            answ = max(answ, top.d);
            q.pop();
            if (top.node->left != nullptr) {
                q.push({top.node->left, top.d + 1});
            }
            if (top.node->right != nullptr) {
                q.push({top.node->right, top.d + 1});
            }
        }
        return answ;
    }
};
