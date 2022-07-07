# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def deleteDuplicates(self,head):
        node,cur = head,head
        nodeSet = set()
        if not head:
            return None
        nodeSet.add(head.val)
  
        while(node.next != None):
            if(node.next.val not in nodeSet):
                cur.next = node.next
                cur = cur.next
                nodeSet.add(cur.val)
            node = node.next
   
        cur.next = None
   
        return head
    
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = head
#         if head == None:
#             return None
#         while (current.next != None) :
#             if current.val == current.next.val:
#                 current.next = current.next.next 
#             else :
#                 current = current.next
         
                
#         return head
    
        