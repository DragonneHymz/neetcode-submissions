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
        if head == None:
            return
        hashMap = {}
        head2 = head
        while head2:
            hashMap[head2] = Node(head2.val)
            head2 = head2.next
        head2 = head
        while head2:
            hashMap[head2].random = hashMap.get(head2.random)
            hashMap[head2].next = hashMap.get(head2.next)
            head2 = head2.next
        return hashMap[head]

