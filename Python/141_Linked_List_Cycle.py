# Definition for singly-linked list.
from operator import truediv


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def answer(head):
    while head:
        if head.val == None:
            return True
        head.val = None
        head = head.next
    return False
        
if __name__ == "__main__":
    head = ListNode(3)
    tail = head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = tail

    print(answer(head))
    