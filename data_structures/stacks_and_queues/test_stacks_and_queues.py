import pytest
from stacks_and_queues import Node, Stack, Queue

stack = Stack()
queue = Queue()

def test_push_to_stack():
    """Can successfully push onto a stack"""
    stack.push(4)
    expected = 4
    actual = stack.top.value
    assert actual == expected

def test_multiple_values_to_stack():
    """Can successfully push multiple values onto a stack"""
    stack.push(2)
    stack.push(3)
    expected = 2
    actual = stack.top.next.value
    assert actual == expected

def test_pop_stack():
    """Can successfully pop off the stack"""
    stack.push(1)
    expected = 1
    assert stack.pop() == expected

def test_empty_stack_after_multiple_pops():
    """Can successfully empty a stack after multiple pops"""
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek_stack():
    """Can successfully peek the next item on the stack"""
    stack.push(6)
    stack.push(9)
    expected = 9
    actual = stack.peek()
    assert actual == expected

def test_instantiate_empty_stack():
    """Can successfully instantiate an empty stack"""
    empty_stack = Stack()
    assert empty_stack

def test_enqueue_to_queue():
    """Can successfully enqueue into a queue"""
    queue.enqueue('first')
    actual = queue.front.value
    expected = 'first'
    assert actual == expected

def test_enqueue_multiple_values():
    """Can successfully enqueue multiple values into a queue"""
    queue.enqueue('second')
    queue.enqueue('third')
    actual = queue.front.next.value
    expected = 'second'
    assert actual == expected

def test_dequeue_test():
    """Can successfully dequeue out of a queue the expected value"""
    queue.enqueue('fourth')
    expected = 'first'
    assert queue.dequeue() == expected

def test_queue_peek():
    """Can successfully peek into a queue, seeing the expected value"""
    assert queue.peek() == 'second'

def test_empty_queue_after_dequeue():
    """Can successfully empty a queue after multiple dequeues"""
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() == True

def test_instantiate_queue():
    """Can successfully instantiate an empty queue"""
    queue = Queue()
    assert queue
