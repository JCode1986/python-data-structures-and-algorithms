from 

def merge_lists(list1, list2): 

    if list1 == None:
        return list2
    if list2 == None:
        return list1

    a_curr = list1.head
    b_curr = list2.head

    while a_curr and b_curr: 
        if a_curr:
            a_ref = a_curr.next
        if b_curr:
            b_ref = b_curr.next
        if a_curr:
            a_curr.next = b_curr
        if b_curr: 
            b_curr.next = a_ref 
            
        a_curr = a_ref
        b_curr = b_ref

    return a_curr 