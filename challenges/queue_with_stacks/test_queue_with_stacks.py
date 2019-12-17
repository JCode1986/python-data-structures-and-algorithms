from queue_with_stacks import PseudoQueue
import pytest

q = PseudoQueue()

def test_one():
    """Can succesfully enqueue to Stack"""
    q.enqueue(1)
    q.enqueue(2)
    actual = q.stack.peek()
    expected = 2
    assert actual == expected

def test_two():
    """Can succesfully dequeue from Stack"""
    q.enqueue(3)
    q.enqueue(4)    
    actual = q.dequeue()
    expected = 1
    assert actual == expected
