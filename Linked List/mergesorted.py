class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      
        self.next = next

def merget(list1, list2):
    d = ListNode() # pretend ListNode exist 
    head = d 

    while list1 and list2:
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next
        head = head.next
    head.next = list1 or list2

    return d.next