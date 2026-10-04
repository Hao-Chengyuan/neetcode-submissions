# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pt, fast_pt = head, head
        
        while fast_pt.next is not None and fast_pt.next.next is not None:
            slow_pt = slow_pt.next
            fast_pt = fast_pt.next.next
        
        if fast_pt.next is not None:
            slow_pt = slow_pt.next
        
        return slow_pt