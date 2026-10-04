# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # count the number of nodes
        counter = head
        i = 0
        while counter:
            i += 1
            counter = counter.next

        idx_to_remove = i - n

        if idx_to_remove == 0:
            return head.next

        prev = head
        for _ in range(idx_to_remove - 1):
            prev = prev.next

        prev.next = prev.next.next

        return head
