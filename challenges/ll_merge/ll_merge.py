from linked_list import Node, Linked_list

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

if __name__ == "__main__":
    lst1 = Linked_list()
    lst2 = Linked_list()
    lst3 = Linked_list()
    lst1.insert(1)
    lst1.append(2)
    lst1.append(3)
    lst1.append(2)
    lst1.append(1)
    lst2.insert(2)
    lst2.append(4)
    lst2.append(6)
    lst2.append(8)
    lst2.append(10)
    lst3.insert(420)
    lst3.append(69)
    print(lst1.to_string())
    print(lst1.to_string())
    merge_lists(lst1, lst2)
    print(lst1.to_string())
    # print(lst3.to_string())