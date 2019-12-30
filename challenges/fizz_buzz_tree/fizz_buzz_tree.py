# from data_structures.tree.tree import BinaryTree, Node
from tree import BinaryTree, Node, BinarySearchTree

def fizz_buzz_tree(tree):
    new_tree = BinaryTree()

    if not tree.root:
        return 'root is None'

    def fizz_buzz(value):
        if value % 3 and value % 5:
            return 'FizzBuzz'
        elif value % 3:
            return 'Fizz'
        elif value % 5:
            return 'Buzz'
        else:
            return str(value)
        
    def helper(current, new_current = None):
        new_current.value = fizz_buzz(current.value)

        if current.left:
            new_current.left = Node()
            helper(current.left, new_current.left)

        if current.right:
            new_current.right = Node()
            helper(current.right, new_current.right)

    helper(tree.root, new_tree.root)
    return new_tree

if __name__ == "__main__":
    tree = BinaryTree()
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(10)
 

    print(fizz_buzz_tree(bst.pre_order()))
    print(bst.root.value)