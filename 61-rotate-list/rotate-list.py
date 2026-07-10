# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
  
        last = head
        len = 0      
        while last.next != None:
            last = last.next
            len += 1

        len += 1
        k = k%len
        
        if k == 0:
            return head
        
        curr = head
        for i in range(len - k - 1):
            curr = curr.next
        
        last.next = head
        head = curr.next
        curr.next = None

        return head