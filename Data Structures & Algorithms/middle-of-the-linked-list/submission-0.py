# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        i = 0

        while current.next is not None:
            current = current.next
            i += 1

        for _ in range((i+1)//2):
            head = head.next
        newhead = head
        
        return newhead