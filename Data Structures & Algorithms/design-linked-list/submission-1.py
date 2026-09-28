# singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummy.next
        count = index
        while count > 0:
            current = current.next
            count -= 1

        return current.val
        
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        current = self.dummy
    
        while current.next is not None:
            current = current.next

        current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self.size:
            current = self.dummy
            new_node = ListNode(val)

            i = 0
            while i < index:
                current = current.next
                i += 1
            
            new_node.next = current.next
            current.next = new_node

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            current = self.dummy

            i = 0
            while i < index:
                current = current.next
                i += 1
            
            current.next = current.next.next
            self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)