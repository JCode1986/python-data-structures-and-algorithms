class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack(Node):
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        """takes any value as an argument and adds a new node with that value to the top of the stack"""
        self.top = Node(value, self.top)
        self.size += 1

    def pop(self):
        """removes the node from the top of the stack, and returns the node’s value"""
        if self.top is None:
            return 'Stack is empty'
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.size -= 1
        return temp.value

    def peek(self):
        """returns the value of the node located on top of the stack, without removing it from the stack"""
        if not self.top:
            return 'Stack is empty'
        else:
            return self.top.value

    def stack_info(self):
        values = " "
        current = self.top
        while current:
            values += f'{[(current.value)]}-->'
            current = current.next
        return f'Stack size: {self.stack_size()} with Values:{values}None'

    def stack_size(self):
        if not self.top:
            return 'Nothing in Stack'
        return self.size

    def is_empty(self):
        """returns a boolean indicating whether or not the stack is empty"""
        if not self.top:
            return True
        else:
            return False
    
class Queue(Node):
    def __init__(self): 
        self.front = None
        self.size = 0

    def enqueue(self, value):
        """takes any value as an argument and adds a new node with that value to the back of the queue"""
        node = Node(value)
        if not self.front:
            self.front = node
            self.size += 1
            return

        current = self.front
        while current.next:
            current = current.next
        self.size += 1
        current.next = node

    def dequeue(self):
        """removes the node from the front of the queue, and returns the node’s value"""
        if not self.front:
            return 'Queue is empty'
        temp = self.front
        self.front = self.front.next
        temp.next = None
        self.size -= 1
        return temp.value

    def peek(self):
        """returns the value of the node located in the front of the queue, without removing it from the queue"""
        if not self.front:
            return 'Queue is empty'
        else:
            return self.front.value

    def queue_info(self):
        values = " "
        current = self.front
        while current:
            values += f'<--{[(current.value)]}'
            current = current.next
        return f'Queue size: {self.queue_size()} with Values: None{values}'
    
    def queue_size(self):
        return self.size

    def is_empty(self):
        """returns a boolean indicating whether or not the queue is empty"""
        if not self.front:
            return True
        else:   
            return False

if __name__ == "__main__":
    stack = Stack()
    stack.push('k')
    stack.push('c')
    stack.push('a')
    stack.push('t')
    stack.push('S')
    stack.push('bar')
    stack.push('foo')
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
    print(stack.stack_info())

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue('Q')
    queue.enqueue('u')
    queue.enqueue('e')
    queue.enqueue('u')
    queue.enqueue('e')
    queue.dequeue()
    print(queue.peek())
    print(queue.is_empty())
    print(queue.queue_size())
    print(queue.queue_info())

