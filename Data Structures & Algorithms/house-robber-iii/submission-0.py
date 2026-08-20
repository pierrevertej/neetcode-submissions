# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo={}
    def rob(self, root: Optional[TreeNode]) -> int:
        ans=0
        if root in self.memo:
            return self.memo[root]
        elif root==None:
            ans=0
        elif root.right==None and root.left==None:
            ans=root.val
        else:
            ans=max(self.rob(root.right)+self.rob(root.left), root.val+self.robchildren(root.right)+self.robchildren(root.left))
        self.memo[root]=ans
        return ans
    def robchildren(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        return self.rob(root.right)+self.rob(root.left)
    
        