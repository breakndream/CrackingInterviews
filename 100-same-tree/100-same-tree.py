# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
# inorder Traversal -> value가 똑같아도 structurally 다른 경우도 있음
        
        # base case
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        leftValue = self.isSameTree(p.left,q.left)
        rightValue = self.isSameTree(p.right,q.right)
        
        if leftValue and rightValue is True:
            if p.val == q.val:
                return True
            else:
                return False
        else :
            return False