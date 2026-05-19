# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:

            front1 = self.iterator(prev_group, k)
            if not front1:
                break
        
            group_start = prev_group.next
            next_group = front1.next

            prev  = next_group
            curr =  group_start
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            prev_group.next = prev
            prev_group = group_start    
        return dummy.next
        

    def iterator(self, front, k):    
        for i in range(k):
            front = front.next
            if front == None:
                return None
        return front    