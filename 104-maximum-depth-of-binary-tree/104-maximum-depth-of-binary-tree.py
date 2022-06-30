# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        
        if not root:
            return level
    
        queue = deque([root])
        while queue: # 넣고 안 넣고의 차이..
            for i in range(len(queue)):
                
                node = queue.popleft()
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            
            level += 1 
            
        return level 
    
