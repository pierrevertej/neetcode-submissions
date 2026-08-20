# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        dq=deque([[root,root.val]])
        while dq:
            for i in range(len(dq)):
                list=dq.popleft()
                node=list[0]
                if node.val==list[1]:
                    count+=1
                if node.left:
                    dq.append([node.left,max(node.left.val,list[1])])
                if node.right:
                    dq.append([node.right,max(node.right.val,list[1])])
        return count