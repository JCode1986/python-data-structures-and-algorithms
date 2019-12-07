class Linked_list:
  def __init__(self, head = None):
    self.head = head

class Node(Linked_list):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

#insert new node to be head
    def insert(self, value):
        new_node = Node(value)
        new_node.next(self.head)
        self.head = new_node

#returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    def includes(self, value):
        current = self.head
        while current:
            if value == current.value:
                return True
            else:
                current = current.next
            return False

#returns a string representing all the values in the Linked List.
    def to_string(self):
        current = self.head
        while current:
            print(current.value)
        current = current.next


node = Node(1)
print(node)


