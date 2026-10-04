# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # count the number nodes
        i = 1
        counter = head
        while counter.next is not None:
            counter = counter.next
            i += 1
        
        # find the middle node
        new_head = head
        for _ in range(i // 2):
            new_head = new_head.next

        return new_head