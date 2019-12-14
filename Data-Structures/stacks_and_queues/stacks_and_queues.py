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
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        """removes the node from the top of the stack, and returns the node’s value"""
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        """returns the value of the node located on top of the stack, without removing it from the stack"""
        return self.top.value

    def stack_size(self):
        return f'Stack Size: {self.size}'

    def is_empty(self):
        """returns a boolean indicating whether or not the stack is empty"""
        return self.top is None
    
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
        while current:
            if current.next:
                current = current.next
            self.size += 1
        current.next = node

    def dequeue(self):
        """removes the node from the front of the queue, and returns the node’s value"""
        temp = self.front
        self.front = self.front.next
        temp.next = null
        return temp.value

    def peek(self):
        """returns the value of the node located in the front of the queue, without removing it from the queue"""
        return self.front
    
    def queue_size(self):
        return f'Queue Size: {self.size}'

    def is_empty(self):
        """returns a boolean indicating whether or not the queue is empty"""
        return self.front is None
  
if __name__ == "__main__":
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)
    # stack.push('hello world')
    # stack.push('bar')
    # stack.push('foo')
    # print(stack.stack_size())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.peek())
    # print(stack.is_empty())

    queue = Queue()
    print(queue.enqueue(1))
    # queue.enqueue(2)
    # queue.enqueue(3)
    # queue.enqueue(34)
    # queue.dequeue()
    print(queue)
    # print(queue.is_empty())
    # print(queue.queue_size())

