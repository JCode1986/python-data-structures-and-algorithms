from stacks_and_queues import Queue, Node

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def breadth_add(self, value):
        """Method that takes in a value, and creates nodes with given value in level order"""

        node = Node(value)

        if not self.root:
            self.root = node
            return

        q = Queue()

        q.enqueue(self.root)

        while not q.is_empty():

            current = q.dequeue()

            if current.left:
                q.enqueue(current.left)
            else:
                current.left = node
                break

            if current.right:
                q.enqueue(current.right)
            else:
                current.right = node
                break

    def pre_order(self, node = None, result = []):
        node = node or self.root        

        result.append(node.value)

        if node.left:
            self.pre_order(node.left, result)

        if node.right:
            self.pre_order(node.right, result)

        return result
    
    def in_order(self, node = None, result = []):

        node = node or self.root

        if node.left:
            self.pre_order(node.left, result)
        result.append(node.value)

        if node.right:
            self.pre_order(node.right, result)

        return result        

    def post_order(self, node = None, result = []):

        node = node or self.root

        if node.left:
            self.pre_order(node.left, result)


        if node.right:
            self.pre_order(node.right, result)
        result.append(node.value)

        return result



    def breadth_first(self):
        """Method that returns all values of tree in level order"""

        if not self.root:
            return 'No root'

        result = []
        q = []
        q.append(self.root)

        while q:
            current = q.pop(0)
            result.append(current.value)

            if current.left:
                q.append(current.left)

            if current.right:
                q.append(current.right)

        return result

    def find_maximum_value_recursive(self):
        """Method that recursively traverses through tree, and returns maximum numeric value"""
        result = 0

        if not self.root:
            return 0

        def _walk(node):

            nonlocal result

            if node.value > result:
                result = node.value
            
            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)

        _walk(self.root)
        return result   

    def find_maximum_value_iterative(self):
        """Method that iteratively traverses through tree, and returns maximum numeric value"""
        result = 0        

        if not self.root:
            return result

        nodes_q = []
        nodes_q.append(self.root)

        while nodes_q:
            current = nodes_q.pop(0)
            
            if current.value > result:
                result = current.value

            if current.left:
                nodes_q.append(current.left)
            
            if current.right:
                nodes_q.append(current.right)

        return result
      
class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        current = self.root
        
        while current:
            if value > current.value:

                if not current.right:
                    current.right = node
            else:

                if not current.left:
                    current.left = node
            return

    def contains(self, value):
        current = self.root

        if current.value == value:
            return True
        
        if value > current.value:
            if current.right.value == value:
                return True
        else:

            if current.left.value == value:
                return True

        return False

if __name__ == "__main__":
    tree = BinaryTree()
    bst = BinarySearchTree()
    bst.add(100)
    bst.add(55)
    bst.add(150)
    tree.pre_order()
