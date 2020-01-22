import pytest
from tree import BinaryTree
from stacks_and_queues import Queue
from tree_intersection import tree_intersection

@pytest.fixture
def tree():
    return BinaryTree()


def test_return_empty_list_if_neither_trees_are_present(tree):
    """
    Returns an empty list if one or the other is None
    """
    empty_tree = tree
    actual = tree_intersection(empty_tree, tree)
    expected = []
    assert actual == expected

def test_return_all_common_values_from_both_trees():
    """
    Returns all common values from both trees
    """
    t1 = BinaryTree()
    t2 = BinaryTree()
    t1_list = [2, 6, 1, 5, 10, 9, 3, 2]
    t2_list = [22, 4, 6, 5, 9]
    for num in t1_list:
        t1.breadth_add(num)
    for num in t2_list:
        t2.breadth_add(num)
    actual = tree_intersection(t1, t2)
    expected = [5, 9, 6]
    assert actual == expected