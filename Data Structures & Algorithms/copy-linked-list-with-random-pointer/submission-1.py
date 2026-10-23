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
        copy = head
        while copy is not None:
            copies[copy] = Node(x=copy.val)
            copy = copy.next
        
        copy = head
        while copy is not None:
            copies[copy].next = copies[copy.next]
            copies[copy].random = copies[copy.random]
            copy = copy.next
        
        return copies[head]
        