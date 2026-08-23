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
#include <vector>

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int leftCount = count(root->left)+1;
        if (leftCount==k) {
            return root->val;
        } if (leftCount>k) {
            return kthSmallest(root->left,k);
        }  return kthSmallest(root->right,k-leftCount);
    }

    int count(TreeNode* root) {
        if (root==nullptr) {
            return 0;
        } return 1 + count(root->left) + count(root->right);
    }
};
