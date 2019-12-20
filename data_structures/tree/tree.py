class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

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
    bst.add(10)
    bst.add(5)
    bst.add(1)
    tree.pre_order()
