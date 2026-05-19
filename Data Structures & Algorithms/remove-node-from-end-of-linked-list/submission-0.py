# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow,far = dummy,dummy
        l=1
        while l<n+1:
            far = far.next
            l+=1

        while far.next:
            slow = slow.next
            far = far.next
        
        slow.next = slow.next.next
       
        return dummy.next       