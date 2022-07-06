# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
       #1. length 서로 비교해서 긴 거는 미리 잘라놔.. 그리고 잘라진거에서 pointer 시작해서 
    # 두개 만나면  둘 중에 하나 리턴
    
        lengthNodeA =  headA
        lengthNodeB =  headB
    
        lengthA = lengthB = 0
    
        while lengthNodeA != None:
            lengthA += 1
            lengthNodeA = lengthNodeA.next
        
        while lengthNodeB != None:
            lengthB += 1
            lengthNodeB = lengthNodeB.next
        
        if lengthA > lengthB :
            disparity = lengthA - lengthB
            while disparity != 0:
                headA = headA.next
                disparity -= 1
        else:
            disparity = lengthB - lengthA
            while disparity != 0:
                headB = headB.next
                disparity -= 1
        
        while headA:
            if headA == headB:
                return headA
            else: 
                headA = headA.next
                headB = headB.next
        return None
    
# while A -> while A is None:
# while not A = while A is not None:  
        
        
    
        
        
        
        