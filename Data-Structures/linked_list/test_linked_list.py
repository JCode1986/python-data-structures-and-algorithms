from linked_list import Linked_list, Node
import pytest

def test_one():
    """Can successfully instantiate an empty linked list"""
    expected = {None}
    actual = Linked_list()
    assert actual == expected

def test_two(value):
    """Can properly insert into the linked list"""
    expected = 2
    Linked_list.insert(1)
    actual = Linked_list.insert(2)
    assert actual == expected

# def test_three(value):
#     """The head property will properly point to the first node in the linked list"""
#     expected = -1
#     actual = binary_search(array_one, 12)
#     assert actual == expected

# def test_four():
#     """Can properly insert multiple nodes into the linked list"""
#     expected = -1
#     actual = binary_search(array_one, 12)
#     assert actual == expected

# def test_five():
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