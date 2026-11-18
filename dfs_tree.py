# ==========================================
# Assessment 3.6: DFS Method in Tree
# Student: Jhuswa Latayada
# ==========================================

# Node class for the Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# 1. Preorder DFS (Root -> Left -> Right)
def dfs_preorder(node):
    if node is None:
        return
    print(node.val, end=", ")
    dfs_preorder(node.left)
    dfs_preorder(node.right)


# 2. Inorder DFS (Left -> Root -> Right)
def dfs_inorder(node):
    if node is None:
        return
    dfs_inorder(node.left)
    print(node.val, end=", ")
    dfs_inorder(node.right)


# 3. Postorder DFS (Left -> Right -> Root)
def dfs_postorder(node):
    if node is None:
        return
    dfs_postorder(node.left)
    dfs_postorder(node.right)
    print(node.val, end=", ")


# 4. Iterative DFS (Using Explicit Stack - Preorder)
def dfs_iterative(root):
    if root is None:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.val, end=", ")
        # Right una i-push para Left ang una ma-pop
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


# Driver code to test the DFS methods
if __name__ == "__main__":
    # Constructing the tree:
    #        S
    #       / \
    #      H   W
    #     / \   \
    #    J   U   A
    root = Node('S')
    root.left = Node('H')
    root.right = Node('W')
    root.left.left = Node('J')
    root.left.right = Node('U')
    root.right.left = Node('A')

    print("Preorder (Root, Left, Right):  ", end="")
    dfs_preorder(root)
    print()

    print("Inorder (Left, Root, Right):   ", end="")
    dfs_inorder(root)
    print()

    print("Postorder (Left, Right, Root): ", end="")
    dfs_postorder(root)
    print()
