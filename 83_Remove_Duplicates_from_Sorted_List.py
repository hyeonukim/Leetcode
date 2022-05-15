# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def answer(head):
    if head == None:
        return None
    res = curr = head
    num = curr.val
    while (curr.next != None):
        if curr.next.val != num:
            res.next = curr.next
            num = curr.next.val
            res = res.next
        curr = curr.next
    if curr.val == num:
        res.next = None
    else:
        res.next = curr
    return head

if __name__ == "__main__":
    print("Enter numbers for this question")
    try: 
        arr = []
        while True:
            arr.append(int(input()))
    except:
        print("your input is", arr)
    
    head = curr = ListNode()
    for i in range(len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    head = head.next

    answer(head)
    while (head != None):
        print(head.val)
        head = head.next