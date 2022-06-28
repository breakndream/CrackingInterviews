class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # edge case ) node is None 
        # Make another ListNode named newNode
        
        # recursively check head.next  -> base case : when head.next is None
        # when to 
        # when head.next is None => reached the end
        # that point : 
        new_node = ListNode(None)
        
        def makeItReverse(root) :
            if root == None :
                return None
            
            if root.next == None:
                new_node.next = root
                return 
            else :
                makeItReverse(root.next)
                
        makeItReverse(head)
        return new_node
        
        
  class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None -> prev = ListNode(None)
        
        while head:
            next = head.next
            head.next = prev
            prev = head (head = prev)
            head = next (next = head 두개 차이...=_=)

        return prev -> head return 
