class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def answer(list1, list2):
    res = curr = ListNode()
    while (list1 and list2):
        if (list1.val < list2.val):
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if (list1):
        curr.next = list1
    elif (list2):
        curr.next = list2

    return res.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    ans = answer(l1,l2)
    while (ans != None):
        print(ans.val)
        ans = ans.next
