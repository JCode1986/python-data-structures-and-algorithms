import pytest
from stacks_and_queues import Node, Stack, Queue

@pytest.fixture
def stack():
    return Stack()

@pytest.fixture
def queue():
    return Queue()

def test_push_to_stack(stack):
    """Can successfully push onto a stack"""
    stack.push(4)
    expected = 4
    actual = stack.top.value
    assert actual == expected

def test_multiple_values_to_stack(stack):
    """Can successfully push multiple values onto a stack"""
    stack.push(2)
    stack.push(3)
    expected = 2
    actual = stack.top.next.value
    assert actual == expected

def test_pop_stack(stack):
    """Can successfully pop off the stack"""
    stack.push(1)
    expected = 1
    assert stack.pop() == expected

def test_empty_stack_after_multiple_pops(stack):
    """Can successfully empty a stack after multiple pops"""
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek_stack(stack):
    """Can successfully peek the next item on the stack"""
    stack.push(6)
    stack.push(9)
    expected = 9
    actual = stack.peek()
    assert actual == expected

def test_instantiate_empty_stack(stack):
    """Can successfully instantiate an empty stack"""
    assert stack

def test_enqueue_to_queue(queue):
    """Can successfully enqueue into a queue"""
    queue.enqueue('first')
    actual = queue.front.value
    expected = 'first'
    assert actual == expected

def test_enqueue_multiple_values(queue):
    """Can successfully enqueue multiple values into a queue"""
    queue.enqueue('apple')
    queue.enqueue('orange')
    actual = queue.front.next.value
    expected = 'orange'
    assert actual == expected

def test_dequeue_test(queue):
    """Can successfully dequeue out of a queue the expected value"""
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    expected = 1
    assert queue.dequeue() == expected

def test_queue_peek(queue):
    """Can successfully peek into a queue, seeing the expected value"""
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1

def test_empty_queue_after_dequeue(queue):
    """Can successfully empty a queue after multiple dequeues"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    for num in nums:
        queue.enqueue(num)

    for _ in nums:
        queue.dequeue()

    assert queue.is_empty() == True

def test_instantiate_queue(queue):
    """Can successfully instantiate an empty queue"""
    assert queue

def test_returns_stack_size(stack):
    """Can successfully returns stacks size"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    for num in nums:
        stack.push(num)
    actual = stack.stack_size()
    expect = 8
    assert expect == actual

def test_returns_queue_size(stack):
    """Can successfully returns queue size"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for num in nums:
        stack.push(num)
    actual = stack.stack_size()
    expect = 13
    assert expect == actual
