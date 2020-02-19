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

# def test_five(linked_list):
#     """Will return true when finding a value within the linked list that exists"""
#     expected = -1
#     actual = binary_search(array_one, 12)
#     assert actual == expected

# def test_six():
#     """Can properly insert multiple nodes into the linked list"""
#     expected = -1
#     actual = binary_search(array_one, 12)
#     assert actual == expected

# def test_seve():
#     """Will return false when searching for a value in the linked list that does not exist"""
#     expected = -1
#     actual = binary_search(array_one, 12)
#     assert actual == expected

# def test_eight():
#     """Can properly return a collection of all the values that exist in the linked list"""
#     expected = -1
#     actual = binary_search(array_one, 12)
#     assert actual == expected

# def test_nine(linked_list):
#     """Can properly append to tail of linked list"""
#     linked_list.append(420)
#     actual = linked_list.tail.value
#     expected = 420
#     assert actual == expected
