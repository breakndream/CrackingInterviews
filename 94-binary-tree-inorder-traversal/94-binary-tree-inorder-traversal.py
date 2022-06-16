# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # inorder = left middle right 
        # edge case : empty root- > [] / just the root 
        
        node_values = []
        
        def traverse(root):
            
            if not root : 
                return 
            else:
                traverse(root.left)
                node_values.append(root.val)
                traverse(root.right)
            
        traverse(root)
        return node_values
        
                    
        