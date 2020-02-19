from fizz_buzz_tree import fizz_buzz_tree, Node, BinaryTree, BinarySearchTree
import pytest

@pytest.fixture
def tree():
    return BinaryTree()

@pytest.fixture
def bst():
    return BinarySearchTree()

def test_if_root_is_none(tree):
    actual = fizz_buzz_tree(tree)
    expected = 'root is None'
    assert actual == expected

# def test_fizz_buzz_helper_on_root_value(tree, bst):
#     bst.add(3)
#     fizz_buzz_tree(bst)  
#     actual = bst.root.value
#     expected = 0
#     assert actual == expected
