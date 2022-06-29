# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # edge case : what if the given node is the first / last one -> it is guaranteed?
        # key point : how do we access the previous node?
        
        # 4 -> 5 -> 6 -> 7   5
        # 4- > 5 -> 7
        dummyNode = ListNode(node.next.val)
        node.next = node.next.next
        node.val = dummyNode.val  
            