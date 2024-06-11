# swap nodes in  pairs in linkedlist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        second.next = first
        current.next = second
        current = first

    return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
new_head = swapPairs(head)


while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
