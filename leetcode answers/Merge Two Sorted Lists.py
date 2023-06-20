# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        INPUT: l1 and l2, two linked lists
        OUTPUT: a single combinded list in order
        SOLUTION:
        
        dummy
        tail 
        
        return dummy.next
        1, 1, 2, 3,  4, 4, 5, 6, 7, 
        '''
        dummy, tail, l1, l2 = ListNode(), ListNode(), list1, list2
        dummy.next = tail
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next.next