class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      
        self.next = next

def removeDups(head):
    t = set()
    d = ListNode(0, head)
    d.next = head
    prev = d
    curr = head
    while curr:
        if curr.val in t:
            prev.next = curr.next
        else:
            t.add(curr.val)
            prev = curr
        curr = curr.next
    return d.next

def removeDupsS(head):
    curr = head
    while curr:
        temp = curr
        while temp.next:
            if temp.next.val == curr.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        curr = curr.next
    return head 

def removeNthFromEnd(head, n):
    res = ListNode(0, head)
    dummy = res

    for i in range(n):
        head = head.next

    while head:
        head = head.next
        dummy = dummy.next

    dummy.next = dummy.next.next

    return res.next

def deleteMiddle(node):
    temp = node.next
    node.val = temp.val
    node.next = temp.next
      
def sumList(head1, head2):
    dumm = ListNode(0)
    curr = dumm
    carr = 0
    
    while head1 and head2:
        if head1 is None:
            x = 0
        else:
            x = head1.val
        if head2 is None:
            y = 0
        else:
            y = head2.val
    
        summ =  carr + x + y
        carr = summ // 10
        curr.next = ListNode(summ % 10)
        curr = curr.next
        
        head1 = head1.next
        head2 = head2.next
    return dumm.next

def findLoopStart(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head 
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    if fast is None or fast.next is None:
        return None
    
    slow = head
    
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow
    

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
    

def main():
    print("LinkedList")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(4)))))
    print_list(head)
    
    print("Remove Dups")
    head = removeDupsS(head)
    print_list(head)
    
    print()

    print("Remove Nth")
    head = removeNthFromEnd(head, 1)
    print_list(head)
    
    print()
    
    print("LinkedList")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(4)))))
    print_list(head)
    
    print()
    
    print("Delete Middle")
    deleteMiddle(head.next.next)
    print_list(head)
    

    
    print()
    head1 = ListNode(3, ListNode(1, ListNode(5)))
    head2 = ListNode(5, ListNode(9, ListNode(2)))

    print("Sum of lists")
    temp = sumList(head1, head2)
    print_list(temp)
    
    print()
    node_a = ListNode('A')
    node_b = ListNode('B')
    node_c = ListNode('C')
    node_d = ListNode('D')
    node_e = ListNode('E')

    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    node_d.next = node_e
    node_e.next = node_c 
    
    print("Finding loop cycle")
    start = findLoopStart(node_a)
    print(start.val)        
    


if __name__ == '__main__':
    main()



