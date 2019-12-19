from tree import Node, BinaryTree, BinarySearchTree
import pytest

tree = BinaryTree()

def instantiate_empty_tree():
    """Can successfully instantiate an empty tree"""
    assert tree._root is None

def instantiate_tree_with_single_root_node():
    """Can successfully instantiate a tree with a single root node"""
    tree.add('I am the root')
    assert tree._root.value == 'I am the root'

def add_left_and_right_to_root():
    """Can successfully add a left child and right child to a single root node"""
    tree.add(100)
    tree.add(50)
    tree.add(150)

    assert tree._root.value == 100
    assert tree._root.left.value == 50
    assert tree._root.right.value == 150

def pre_order_traversal():
    """Can successfully return a collection from a preorder traversal"""
    tree.add(100)
    tree.add(50)
    tree.add(150)

    expected = [100,50,150]
    actual = tree.pre_order()

    assert expected == actual

def inorder_traversal():
    """Can successfully return a collection from an inorder traversal"""
    tree.add(100)
    tree.add(50)
    tree.add(150)

    expected = [50,100, 150]
    actual = tree.in_order()

    assert expected == actual


def postorder_traversal():
    """Can successfully return a collection from a postorder traversal"""
    tree.add(100)
    tree.add(50)
    tree.add(150)

    expected = [50,150, 100]
    actual = tree.post_order()

    assert expected == actual

