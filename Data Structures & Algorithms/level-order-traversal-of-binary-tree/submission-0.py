# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        tree=[[root.val]]
        currentLvl=[root]
        nextLvl=[]
        nextVals=[]
        while True:
            for node in currentLvl:
                if node.left!=None:
                    nextLvl.append(node.left)
                    nextVals.append(node.left.val)
                if node.right!=None:
                    nextLvl.append(node.right)
                    nextVals.append(node.right.val)
            if not nextLvl:
                return tree
            currentLvl=nextLvl
            tree.append(nextVals)
            nextLvl=[]
            nextVals=[]