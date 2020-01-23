from stacks_and_queues import Queue
from tree import BinaryTree

def tree_intersection(tree_one, tree_two):
    """
    Function that takes in two binary trees, and returns a list of all common values in both trees
    In: 2 parameters - 2 trees
    Out: List of all common values found in both trees
    """

    if tree_one is None or tree_two is None:
        return []

    seen = set()
    result = []
    
    def walk_one(node):

        if node is None:
            return

        seen.add(node.value)

        walk_one(node.left)
        walk_one(node.right)

    walk_one(tree_one.root)

    def walk_two(node):
 
        if node is None:
            return

        if node.value in seen:
            result.append(node.value)

        walk_two(node.left)
        walk_two(node.right)
    
    walk_two(tree_two.root)
    return result
    

if __name__ == "__main__":
    t1 = BinaryTree()
    t2 = BinaryTree()
    t1_list = [2, 6, 1, 5, 10, 9, 3, 2]
    t2_list = [22, 4, 6, 5, 9]
    for num in t1_list:
        t1.breadth_add(num)
    for num in t2_list:
        t2.breadth_add(num)
    print(t1.breadth_first())
    print(t2.breadth_first())
    print(tree_intersection(t1, t2))