class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Linked_list:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def insert(self, value):
        """insert new node to be head"""
        new_node = Node(value) 
        new_node.next = self.head 
        self.head = new_node

    def includes(self, value):
        """
        Given a value as a parameter, return a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
        """
        current = self.head
        while current:
            if value == current.value:
                return True
            current = current.next
        return False

    def to_string(self):
        """returns a string representing all the values in the Linked List."""
        values = " "
        current = self.head
        while current:
            values += f'{[(current.value)]}-->'
            current = current.next
        return values

    def append(self, value):
        node = Node(value)
        current = self.head
        while current:
            if current.next == None:
                current.next = node
                node.next = None
                self.tail = node
            current = current.next

    def insert_before(self, value, new_value):
        node = Node(new_value)
        current = self.head
        temp = self.head
        while current:
            if current.value == value:
                temp.next = node
                node.next = current   
            temp = current                 
            current = current.next

    def insert_after(self, value, new_value):
        node = Node(new_value)
        current = self.head
        temp = self.head
        while current:
            if current.value == value: 
                temp = current.next
                current.next = node
                node.next = temp
            current = current.next

    def kth_from_end(self, k): 
        length =  0
        current = self.head

        while current.next:
            current = current.next
            length += 1
        count = length - k
        current = self.head
        if k > count:
            return 'Exception'
        while count > 0:
            current = current.next
            count -= 1
        print(current.value)
        return current.value

    def is_palindrome(self, lst):
        current = lst.head       
        values = [] 
        while current: 
            values.append(current.value) 
            current = current.next
        string = "".join(values)
        return string == string[::-1]

    def reverse(self, lst):
        pass
                

if __name__ == "__main__":
    lst = Linked_list()
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
    # print(lst1.to_string())
    # print(lst1.to_string())
    # lst.merge_lists(lst1, lst2)
    # print(lst3.to_string())
    print(lst2.to_string())
    print(lst.is_palindrome(lst2))
    # print(lst.to_string())
    # lst.insert_after(2, 420)
    # lst.insert_before(69, 30)
    # lst.kth_from_end(3)
    # print(lst.includes('a'))
    # print(lst.includes(1))




