from tree import Node, BinaryTree, BinarySearchTree
import pytest

@pytest.fixture
def bst():
    return BinarySearchTree()

@pytest.fixture
def tree():
    return BinaryTree()

def test_instantiate_empty_tree(tree):
    """Can successfully instantiate an empty tree"""
    assert tree.root is None

def test_instantiate_tree_with_single_root_node(bst):
    """Can successfully instantiate a tree with a single root node"""
    bst.add('I am the root')
    assert bst.root.value == 'I am the root'

def test_add_left_and_right_to_root(bst):
    """Can successfully add a left child and right child to a single root node"""
    bst.add(100)
    bst.add(50)
    bst.add(150)

    assert bst.root.value == 100
    assert bst.root.left.value == 50
    assert bst.root.right.value == 150

def test_pre_order_traversal(bst):
    """Can successfully return a collection from a preorder traversal"""
    bst.add(100)
    bst.add(50)
    bst.add(150)

    expected = [100,50,150]
    actual = bst.pre_order()

    assert expected == actual

def test_inorder_traversal(bst):
    """Can successfully return a collection from an inorder traversal"""
    bst.add(100)
    bst.add(50)
    bst.add(150)

    expected = [50,100, 150]
    actual = bst.in_order()

    assert expected == actual


def test_post_order_traversal(bst):
    """Can successfully return a collection from a post order traversal"""
    bst.add(100)
    bst.add(50)
    bst.add(150)

    expected = [50,150, 100]
    actual = bst.post_order()

    assert expected == actual

def test_contains_method_true_root(bst):
    bst.add(100)
    bst.add(50)
    bst.add(150)
    
    expected = True
    actual = bst.contains(100)
    assert expected == actual

def test_contains_method_false(bst):
    bst.add(100)
    bst.add(50)
    bst.add(150)
    
    expected = False
    actual = bst.contains(99)
    assert expected == actual

def test_contains_method_true_children(bst):
    bst.add(100)
    bst.add(50)
    bst.add(150)
    
    expected = True
    actual = bst.contains(150)
    assert expected == actual
