def reverse(head):
    p = None 
    c = head

    while c != None: 
        temp = c.next
        c.next = p
        p = c
        c = temp

    return p