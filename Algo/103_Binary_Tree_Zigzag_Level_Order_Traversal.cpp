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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        if (root != nullptr) {
            q.push(root);
        } else {
            return {};
        }
        vector<vector<int>> answ;
        bool f = false;
        while (!q.empty()) {
            auto sz = q.size();
            vector<int> v(sz);
            for (int i = 0; i < sz; ++i) {
                auto top = q.front();
                q.pop();
                v[i] = top->val;
                if (top->left != nullptr) {
                    q.push(top->left);
                }
                if (top->right != nullptr) {
                    q.push(top->right);
                }
            }
            if (f) {
                reverse(v.begin(), v.end());
            }
            f ^= 1;
            answ.push_back(v);
        }
        return answ;
    }
};
