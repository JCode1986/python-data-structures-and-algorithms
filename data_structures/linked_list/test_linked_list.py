import pytest
from linked_list import Linked_list, Node

@pytest.fixture
def linked_list():
    return Linked_list()


def test_one(linked_list):
    """Can successfully instantiate an empty linked list"""
    assert linked_list

def test_two(linked_list):
    """Can properly insert into the linked list"""
    expected = 2
    linked_list.insert(1)
    linked_list.insert(2)
    actual = linked_list.head.value
    assert actual == expected

def test_three(linked_list):
    """Can properly insert multiple nodes into the linked list"""
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    expected = [3, 2, 1]
    actual = [linked_list.head.value, linked_list.head.next.value, linked_list.head.next.next.value]
    assert actual == expected

def test_four(linked_list):
    """Will return boolean if a value in the linked list exists"""
    expected = [True, False]
    linked_list.insert(1)
    linked_list.insert(2)
    actual = [linked_list.includes(1), linked_list.includes(9999)]
    assert actual == expected

def test_five(linked_list):
    """Can properly return a collection of all the values that exist in the linked list"""
    nums = [4, 3, 2, 1, 0]
    for num in nums:
        linked_list.insert(num)
    expected = "[0]-->[1]-->[2]-->[3]-->[4]-->"
    actual = linked_list.to_string()
    assert actual == expected

def test_six(linked_list):
    """Can append to head of an empty linked list"""
    linked_list.append(420)
    actual = linked_list.head.value
    expected = 420
    assert actual == expected

def test_seven(linked_list):
    """Can properly append to tail of linked list"""
    linked_list.insert(1)
    linked_list.append(420)
    actual = linked_list.tail.value
    expected = 420
    assert actual == expected

# def test_eight(linked_list):
#     """Can properly insert before a specific node"""
#     nums = [4, 3, 2, 1, 0]
#     for num in nums:
#         linked_list.append(num)
#     actual = linked_list.insert_before(23, 2)
#     expected = linked_list.head.next.next.value
#     assert actual == expected
