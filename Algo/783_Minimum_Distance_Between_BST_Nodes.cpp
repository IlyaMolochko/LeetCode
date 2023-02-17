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
    int answ;
    TreeNode *prev_;
public:
    void inorder(TreeNode *root) {
        if (root == nullptr) {
            return;
        }
        inorder(root->left);
        if (prev_ != nullptr) {
            answ = min(answ, root->val - prev_->val);
        }
        prev_ = root;
        inorder(root->right);
    }

    int minDiffInBST(TreeNode* root) {
        prev_ = nullptr;
        answ = numeric_limits<int>::max();
        inorder(root);
        return answ;
    }
};
