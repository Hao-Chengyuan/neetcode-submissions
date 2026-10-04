# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        new_head = head
        while new_head is not None and new_head.val == val:
            new_head = new_head.next

        if new_head is None:
            return new_head
        
        curr = new_head.next
        prev = new_head

        # loop over all the nodes
        while curr is not None:
            # find the nodes that have the same value as val
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return new_head
