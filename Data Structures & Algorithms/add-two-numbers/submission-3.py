# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        dummy = new_head

        carry = 0
        while l1 and l2:
            sum_two = l1.val + l2.val
            in_place = sum_two % 10
            dummy.next = ListNode(val=(in_place+carry) % 10)
            carry = sum_two // 10 + ((in_place + carry) // 10)

            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        
        while l1:
            in_place = (l1.val+carry) % 10
            dummy.next = ListNode(val=in_place)
            carry = (l1.val+carry) // 10
            l1 = l1.next
            dummy = dummy.next

        while l2:
            in_place = (l2.val+carry) % 10
            dummy.next = ListNode(val=in_place)
            carry = (l2.val+carry) // 10
            l2 = l2.next
            dummy = dummy.next

        dummy.next = ListNode(val=carry) if carry != 0 else None
        
        return new_head.next
