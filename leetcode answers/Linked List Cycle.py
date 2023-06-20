class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        INPUT: head
        OUTPUT: true if there's a cycle, false if not
        SOLUTION:
        
        None
        
        while head:
            if head == None:
                return False
            elif head.val == False: 
                return True
            else:
                head.val = False
                head = head.next
        
        '''
        
        
        while head:
            if head == None:
                return False
            elif head.val == False: 
                return True
            else:
                head.val = False
                head = head.next