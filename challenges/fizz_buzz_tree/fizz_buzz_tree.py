# from data_structures.tree.tree import BinaryTree, Node
from tree import BinaryTree, Node

def fizz_buzz_tree(tree):
    new_tree = BinaryTree()

    if not tree.root:
        return new_tree

    def helper(current):
        node = Node(current.value)
        
        if node.value % 15 == 0:
            return 'FizzBuzz'
        elif node.value % 3:
            return 'Fizz'
        elif node.value % 5:
            return 'Buzz'
        else:
            return str(current.value)
        
        if current.left:
            node.left = helper(current.left)

        if current.right:
            node.right = helper(current.right)

        return node

    new_tree.root = helper(tree.root)
    return new_tree