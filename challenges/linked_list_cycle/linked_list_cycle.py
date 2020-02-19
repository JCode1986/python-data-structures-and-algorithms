from linked_list import Node, Linked_list

def is_cycle(node):
    if not node or not node.next:
        return False

    slow, fast = node

    while slow:
        if fast.next or fast.next.next:
            return False

        if slow == fast:
            return True

if __name__ == "__main__":
    linked_list = Linked_list()
    print(linked_list)

