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
        
    def helper(current):
        # node = Node(fizz_buzz(current.value))
        current = current or tree.root
        node = Node(fizz_buzz(current.value))

        print(node)
        if current.left:
            node.left = helper(current.left)

        if current.right:
            node.right = helper(current.right)

        return node

    new_tree.root = helper(tree.root)
    return new_tree

if __name__ == "__main__":
    tree = BinaryTree()
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(10)
    bst.add(15)

    # print(fizz_buzz_tree(bst.pre_order()))
    print(bst.root.left.value)