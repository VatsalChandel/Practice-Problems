class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      
        self.next = next
        
def removeNthFromEnd(head, n: int):
        res = ListNode(0, head)
        dummy = res

        for i in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next

def removeHead(head):
    head = head.next
    return head


def removeANode(head, k):
    d = ListNode(0)
    d.next = head
    prev = d
    curr = head
    while curr:
        if curr.val == k:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    
    return d.next
    

head3 = ListNode(4, None)
head21 = ListNode(3, head3)
head2 = ListNode(3, head21)
head1 = ListNode(2, head2)
head = ListNode(1, head1)

head = removeANode(head, 4)

#removeNthFromEnd(head, n = 2)

while head:
    print(head.val)
    head = head.next
    

