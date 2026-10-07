# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        # find the left node
        leftnode_prev = dummy
        for _ in range(left-1):
            leftnode_prev = leftnode_prev.next
        leftnode = leftnode_prev.next

        prev = leftnode
        curr = leftnode.next
        for _ in range(right - left):
            oldnext = curr.next
            curr.next = prev
            prev = curr
            curr = oldnext
        
        leftnode.next = curr
        leftnode_prev.next = prev
        
        return dummy.next