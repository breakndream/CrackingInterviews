# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True 
        if not root.left and not root.right:
            return True
        
        return self.mirror(root.left, root.right)

    def mirror(self, left, right):
        if not left and not right:
            return True
        else:
            if not left and right:
                return False
            if left and not right:
                return False
        
        if left.val == right.val :
            outerTree = self.mirror(left.left, right.right)
            innerTree = self.mirror(left.right, right.left)
            if outerTree and innerTree is True:
                return True
            else:
                return False
        else :
            return False
            
    
        