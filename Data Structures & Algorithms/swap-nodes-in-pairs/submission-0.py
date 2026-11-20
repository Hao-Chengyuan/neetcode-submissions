# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        dummy = ListNode(0, head)
        new_head = dummy
        
        while curr is not None and curr.next is not None:
            if curr.next.next is None:
                nxt = curr.next
                new_head.next = nxt
                nxt.next = curr
                curr.next = None
                return dummy.next
            else:
                nxt = curr.next
                after = nxt.next
                new_head.next = nxt
                nxt.next = curr
                new_head = new_head.next.next
                curr = after
                nxt = curr.next
        
        if curr is not None:
            new_head.next = curr
        
        return dummy.next