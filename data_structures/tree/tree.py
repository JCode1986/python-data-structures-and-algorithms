class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, node):
        current = self.root
        result = []

        if current:
            result.append(current.value)

            if current.left:
                self.pre_order(current.left)

            if current.right:
                self.pre_order(current.right)

        return result
    
    def post_order(self, node):
        current = self.root
        result = []

        if current:
            if current.left:
                result.append(current.value)
                self.pre_order(current.left)

            if current.right:
                self.pre_order(current.right)

        return result        

    def in_order(self, node):
        current = self.root
        result = []
        
        if current:
            
            if current.left:
                self.pre_order(current.left)
            result.append(current.value)

            if current.right:
                self.pre_order(current.right)
        return result    

class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        node = Node(value)
        current = self.root

        if not current:
            current = node
            return
        
        if node.value > current.value:

            if not current.right:
                current.right = node
        else:

            if not current.left:
                current.left = node


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