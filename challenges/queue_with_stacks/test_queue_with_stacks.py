from queue_with_stacks import PseudoQueue
import pytest

q = PseudoQueue()

def test_one():
    """Can succesfully enqueue to Stack"""
    q.enqueue(1)
    actual = q.enqueue(2)
    expected = 'fail'
    assert actual == epxected

def test_two():
    """Can succesfully dequeue from Stack"""
    q.enqueue(3)
    q.enqueue(4)    
    actual = q.dequeue()
    expected = 'test'
    assert actual == expected