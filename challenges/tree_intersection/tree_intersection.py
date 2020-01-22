
def tree_intersection(tree_one, tree_two):
    """
    Function that takes in two binary trees, and returns a list of all common values in both trees
    In: 2 parameters - 2 trees
    Out: List of all common values found in both trees
    """
    seen = set()
    result = []
    
    def walk_one(node):
        nonlocal seen

        if node is None:
            return

        seen.add(node.value)

        walk_one(node.left)
        walk_one(node.right)

    walk_one(tree_one.root)

    def walk_two(node):
        nonlocal seen
        nonlocal result

        if node is None:
            return

        if node.value in seen:
            result.append(node.value)

        walk_one(node.left)
        walk_one(node.right)

    walk_two(tree_two.root)
    
    return result

