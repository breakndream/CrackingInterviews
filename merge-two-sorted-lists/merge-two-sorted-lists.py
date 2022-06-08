# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # new_list = []
        # while ! list1node.isEmpty() && list2node.isEmpty() {
        # list1 첫번째 노드값  vs list 2 첫번째 노드값
        # if (list1 첫번째 노드값 < list 2 첫번째 노드값)
             # new_list.append (list1 첫번째 노드)
             #list1.listnode = list1.listnode.next
        # else 
            # new_list.append (list2 첫번째 노드)
            # list2.listnode = list2.listnode.next
        # }
        # 하나만 list 가 끝날 경우
        # if (list1node.next.isEmpty()) {
        #    new_list.append[list2node.next , ]
        #}
        # if (list2node.next.isEmpty()) {
        #    new_list.append[list1node.next , ]
        #}
        # return new_list[0]
        
        
        new_list = []
        while list1 and list2 :
            if list1.val < list2.val:
                new_list.append(list1)
                list1 = list1.next
            else :
                new_list.append(list2)
                list2 = list2.next
        while not list1 and list2 :
            new_list.append(list2)
            list2 = list2.next
        while not list2 and list1 :
            new_list.append(list1)
            list1 = list1.next
        for i in range(len(new_list)- 1) :
            new_list[i].next = new_list[i+1]
        return new_list[0] if new_list else None
        
    
                
            