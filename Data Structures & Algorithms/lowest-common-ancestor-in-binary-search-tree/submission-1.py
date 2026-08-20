# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        target=[q.val,p.val]
        if p.val<q.val:
            target=[p.val,q.val]
        def search(node):
            if node.val>=target[0] and node.val<=target[1]:
                return node
            if node.val>target[0]:
                return search(node.left)
            else:
                return search(node.right)
        return search(root)