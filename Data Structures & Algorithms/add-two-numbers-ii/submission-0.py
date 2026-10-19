# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverselist(l: Optional[ListNode]):
            prev = None
            curr = l
            while curr is not None:
                saved_next = curr.next
                curr.next = prev
                prev = curr
                curr = saved_next
            return prev

        l1_r = reverselist(l1)
        l2_r = reverselist(l2)
        l12_r = ListNode()
        head = l12_r
        carry = 0

        while l1_r and l2_r:
            node_sum = l1_r.val + l2_r.val + carry
            head.next = ListNode(val=node_sum % 10)
            carry = node_sum // 10
            l1_r = l1_r.next
            l2_r = l2_r.next
            head = head.next
        
        lc = l1_r if l1_r else l2_r
        while lc:
            node_sum = lc.val + carry
            head.next = ListNode(val=node_sum % 10)
            carry = node_sum // 10
            head = head.next
            lc = lc.next
        
        if carry:
            head.next = ListNode(val=carry)

        return reverselist(l12_r.next)
