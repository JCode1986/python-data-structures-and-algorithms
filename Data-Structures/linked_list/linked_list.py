class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Linked_list:
    def __init__(self, head = None):
        self.head = head

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
            current = current.next

    def insert_before(self, value, new_value):
        pass

    def insert_after(self, value, new_value):
        pass


if __name__ == "__main__":
    lst = Linked_list()
    print(type(lst))
    lst.insert(1)
    lst.insert(2)
    lst.insert(3)
    lst.insert(4)
    lst.append(69)
    print(lst.includes('a'))
    print(lst.includes(1))
    print(lst.to_string())




