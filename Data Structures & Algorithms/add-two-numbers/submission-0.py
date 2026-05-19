# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode(0)
        second = ListNode(0)
        third = ListNode(0)
        dummy = third

        first.next = l1
        second.next = l2

        carry = 0

        while first.next or second.next or carry:
            f1 = first.next.val if first.next else 0
            s1 = second.next.val if second.next else 0
            sum1 = carry + f1 + s1
            carry = sum1 // 10
            val = sum1 % 10
            third.next = ListNode(val)

            if first.next:
                first = first.next
            if second.next:
                second = second.next    
           
            third = third.next
            
        return dummy.next    
