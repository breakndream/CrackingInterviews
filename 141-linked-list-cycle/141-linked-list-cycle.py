# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1. single node -> return False
        # 2. traverse nodes -> if that value is in  a set. return True. : infinite loop
        # 3 to return false: linked list is finite.
        
        visit = set()

        
        while head != None:
            if head not in visit:
                visit.add(head)
                head = head.next
            else :
                return True
        return False
            
            
        
        