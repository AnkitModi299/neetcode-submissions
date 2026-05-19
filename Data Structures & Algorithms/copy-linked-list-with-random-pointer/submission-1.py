"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dict1 = {}
        curr = head
        while curr:
            dict1[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clone = dict1[curr]
            clone.next = dict1.get(curr.next)
            clone.random = dict1.get(curr.random)
            curr = curr.next

        return dict1[head]            