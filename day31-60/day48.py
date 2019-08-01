class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_tree(preorder, inorder):

    if not preorder or not inorder:
        return None

    rootchar = preorder[0]

    if len(preorder) == 1:
        return Node(rootchar)
    
    rootnode = Node(rootchar)

    for i, char in enumerate(inorder):
        if char == rootchar:
            rootnode.left = get_tree(preorder=preorder[1: i+1], inorder=inorder[:i])
            rootnode.right = get_tree(preorder=preorder[i+1:], inorder=inorder[i+1:])
    
    return rootnode
    
tree = get_tree(preorder=['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                inorder=['d', 'b', 'e', 'a', 'f', 'c', 'g'])
assert tree.val == 'a'
assert tree.left.val == 'b'
assert tree.left.left.val == 'd'
assert tree.left.right.val == 'e'
assert tree.right.val == 'c'
assert tree.right.left.val == 'f'
assert tree.right.right.val == 'g'

tree = get_tree(preorder=['a', 'b', 'd', 'e', 'c', 'g'],
                inorder=['d', 'b', 'e', 'a', 'c', 'g'])
assert tree.val == 'a'
assert tree.left.val == 'b'
assert tree.left.left.val == 'd'
assert tree.left.right.val == 'e'
assert tree.right.val == 'c'
assert tree.right.right.val == 'g'

preorder = [1, 2, 4, 5, 6]
print(preorder[:3])