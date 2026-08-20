# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        dictEndsRoot={}
        dictMax={}
        def maxEndsRoot(root):
            if root in dictEndsRoot:
                return dictEndsRoot[root]
            ans=0
            if root.left:
                if root.right:
                    ans=max(max(maxEndsRoot(root.left), maxEndsRoot(root.right),0)+root.val,0)
                else:
                    ans=max(max(maxEndsRoot(root.left),0)+root.val,0)
            else:
                if root.right:
                    ans=max(max(maxEndsRoot(root.right),0)+root.val,0)
                else:
                    ans=max(root.val,0)
            dictEndsRoot[root]=ans
            return ans
        def maxPath(root):
            if root in dictMax:
                return dictMax[root]
            if root.left:
                maxERL=maxEndsRoot(root.left)
                if root.right:
                    maxERR=maxEndsRoot(root.right)
                    ans=max(maxPath(root.left), maxPath(root.right), max(maxERL,maxERR)+root.val, maxERL+maxERR+root.val)
                else:
                    ans=max(maxPath(root.left), maxERL+root.val)
            else:
                if root.right:
                    maxERR=maxEndsRoot(root.right)
                    ans=max(maxPath(root.right), maxERR+root.val)
                else:
                    ans=root.val
            dictMax[root]=ans
            return ans
        return maxPath(root)