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
            values += " " + str(current.value)
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
        return current.value


if __name__ == "__main__":
    lst = Linked_list()
    print(type(lst))
    lst.insert(1)
    lst.insert(2)
    lst.insert(3)
    lst.insert(4)
    lst.append(69)
    lst.insert_after(2, 420)
    lst.insert_before(4, 30)
    lst.kth_from_end(3)
    print(lst.includes('a'))
    print(lst.includes(1))
    print(lst.to_string())




