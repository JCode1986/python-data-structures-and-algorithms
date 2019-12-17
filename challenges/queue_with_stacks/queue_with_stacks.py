from stacks_and_queues import Stack 

class PseudoQueue:
    def __init__(self):
        self.stack = Stack()

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        rev_stack = Stack()
        
        while self.stack.top:
            rev_stack.push(self.stack.pop())
        removed = rev_stack.pop()

        while rev_stack.top:
            self.enqueue(rev_stack.pop())
        return removed

if __name__ == "__main__":
    q = PseudoQueue()
    q.enqueue('I am first and on top of stack, pop me!')
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.stack.stack_info())
