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

def test_breadth_root_none(bst):
    expected = 'No root'
    actual = bst.breadth_first()
    assert actual == expected

def test_breadth_return_root_value(bst):
    bst.add(100)

    expected = [100]
    actual = bst.breadth_first()
    assert expected == actual

def test_breadth_return_root_value_with_child(bst):
    bst.add(100)
    bst.add(50)

    expected = [100, 50]
    actual = bst.breadth_first()
    assert expected == actual

def test_breadth_return_root_value_with_children(bst, tree):
    tree.breadth_add('apples')
    tree.breadth_add('bananas')
    tree.breadth_add('cucumbers')
    tree.breadth_add('dates')
    tree.breadth_add(1)
    tree.breadth_add(2)
    tree.breadth_add(3)
    tree.breadth_add(4)

    expected = ['apples', 'bananas', 'cucumbers', 'dates', 1, 2, 3, 4]
    actual = tree.breadth_first()
    assert expected == actual

def test_add_four_nodes(tree):
    tree.breadth_add('apples')
    tree.breadth_add('bananas')
    tree.breadth_add('cucumbers')
    tree.breadth_add('dates')
    assert tree.root.value == 'apples'
    assert tree.root.left.value == 'bananas'
    assert tree.root.right.value == 'cucumbers'
    assert tree.root.left.left.value == 'dates'
    assert tree.root.left.right == None

def test_find_maximum_no_root_iterative(tree):
    expected = 0
    actual = tree.find_maximum_value_iterative()
    assert actual == expected   

def test_find_maximum_num_iterative(tree):
    tree.breadth_add(23)
    tree.breadth_add(19)
    tree.breadth_add(24)
    tree.breadth_add(30)
    tree.breadth_add(16)
    expected = 30
    actual = tree.find_maximum_value_iterative()
    assert expected == actual

def test_find_maximum_no_root_recursive(tree):
    expected = 0
    actual = tree.find_maximum_value_recursive()
    assert actual == expected 

def test_find_maximum_num_recursive(tree):
    tree.breadth_add(23)
    tree.breadth_add(19)
    tree.breadth_add(24)
    tree.breadth_add(300)
    tree.breadth_add(16000)
    expected = 16000
    actual = tree.find_maximum_value_recursive()
    assert expected == actual
