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

        copies = {None: None}
        cp = head
        while cp is not None:
            copies[cp] = Node(cp.val)
            cp = cp.next
        
        cp = head
        while cp is not None:
            copies[cp].next = copies[cp.next]
            copies[cp].random = copies[cp.random]
            cp = cp.next
        
        return copies[head]
