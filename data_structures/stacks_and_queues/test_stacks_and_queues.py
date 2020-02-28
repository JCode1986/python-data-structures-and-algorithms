import pytest
from stacks_and_queues import Node, Stack, Queue

@pytest.fixture
def stack():
    return Stack()

@pytest.fixture
def queue():
    return Queue()


#################
#     Stack     #
#################

def test_instantiate_empty_stack(stack):
    """Can successfully instantiate an empty stack"""
    assert stack

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
    expected = 3
    actual = stack.top.value
    assert actual == expected

def test_pop_stack(stack):
    """Can successfully pop off the stack"""
    stack.push(1)
    expected = 1
    assert stack.pop() == expected

def test_pop_stack_empty(stack):
    """Returns string message if there is nothing to pop in stack"""
    actual = stack.pop()
    expected = 'Stack is empty'
    assert actual == expected

def test_if_stack_is_empty_boolean(stack):
    """Returns boolean is stack is empty"""
    empty_stack = Stack()
    stack.push('mouse')
    actual = [empty_stack.is_empty(), stack.is_empty()]
    expected = [True, False]
    assert actual == expected

def test_empty_stack_after_multiple_pops(stack):
    """Can successfully empty a stack after multiple pops"""
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek_stack(stack):
    """Can successfully peek the top of the stack"""
    stack.push(6)
    stack.push(9)
    expected = 9
    actual = stack.peek()
    assert actual == expected

def test_peek_stack_empty(stack):
    "Returns string message if stack is empty"
    actual = stack.peek()
    expected = 'Stack is empty'
    assert actual == expected

def test_returns_stack_size(stack):
    """Can successfully returns stacks size"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    for num in nums:
        stack.push(num)
    actual = stack.stack_size()
    expect = 8
    assert expect == actual


#################
#     Queue     #
#################

def test_instantiate_queue(queue):
    """Can successfully instantiate an empty queue"""
    assert queue

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

def test_dequeue_empty_queue(queue):
    """Returns string message if queue is empty when dequeueing"""
    actual = queue.dequeue()
    expected = 'Queue is empty'
    assert actual == expected

def test_queue_peek(queue):
    """Can successfully peek into a queue, seeing the expected value"""
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1

def test_queue_empty_peek(queue):
    """Returns string message if queue is empty when peeking"""
    actual = queue.peek()
    expected = 'Queue is empty'
    assert actual == expected

def test_if_queue_is_empty_boolean(queue):
    empty_queue = Queue()
    queue.enqueue('bag')
    actual = [empty_queue.is_empty(), queue.is_empty()] 
    expected = [True, False]
    assert actual == expected

def test_empty_queue_after_dequeue(queue):
    """Can successfully empty a queue after multiple dequeues"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    for num in nums:
        queue.enqueue(num)
    for _ in nums:
        queue.dequeue()
    assert queue.is_empty() == True

def test_returns_queue_size(queue):
    """Can successfully returns queue size"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for num in nums:
        queue.enqueue(num)
    actual = queue.queue_size()
    expect = 13
    assert expect == actual
