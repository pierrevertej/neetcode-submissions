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
    bool isValidBST(TreeNode* root) {
        if (root==nullptr) {
            return true;
        }
        if (root->left != nullptr && root->left->val >= root->val) {
            return false;
        } if (root->right != nullptr && root->right->val <= root->val) {
            return false;
        } return (isValidBSTr(root->left, -1000000001, root->val) && isValidBSTr(root->right, root-> val, 1000000001));
    } bool isValidBSTr(TreeNode* root, int low, int high) {
        if (root==nullptr) {
            return true;
        }
        if (root->left != nullptr && (root->left->val >= root->val || root->left->val <= low)) {
            return false;
        } if (root->right != nullptr && (root->right->val <= root->val || root->right->val >= high)) {
            return false;
        } return (isValidBSTr(root->left, low, root->val) && isValidBSTr(root->right, root-> val, high));
    }
};
