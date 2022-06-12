# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # 1. Do I need to make all elements in List array to nodes?
        # 2. how to sort nodes with the same values?
        
        if not nums: return
        mid = len(nums) //2
        
        # -10,-3,0,5,9
        rootNode = TreeNode(nums[mid])
        rootNode.left = self.sortedArrayToBST(nums[:mid])
        rootNode.right = self.sortedArrayToBST(nums[mid+1:])
        
        return rootNode
        
    
#      def makeBST(self, nums: List[int], left: int, right: int):  
        
        # [-10,-3]
        

        # for node in nums:
        #      if node < :
        #             rootNode.left = makeBST (nums[:halfPoint], root)
                    
#                 BSTarray.append(node)
#                 sortedArrayToBST(nums)
#             else:
#                 BSTarray.append(node)
#                 sortedArrayToBST(nums)
#         print(BSTarray)
                
#if rootNode.left is null:
# else :
# node.val < rootNode.left.val:
# node = rootNode.left.left