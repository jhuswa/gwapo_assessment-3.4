from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_binary_tree():
    # Constructing the binary tree matching your handwritten diagram and DFS order
    root = TreeNode('L')

    # Left subtree branch
    root.left = TreeNode('A')
    root.left.left = TreeNode('A')
    root.left.left.right = TreeNode('Y')

    # Right subtree branch
    root.right = TreeNode('T')
    root.right.left = TreeNode('A')
    root.right.right = TreeNode('D')
    root.right.right.left = TreeNode('A')

    return root


def bfs(root):
    if not root:
        return
    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print("Binary Tree BFS:", " - ".join(result))


def dfs(root):
    # Pre-order DFS: Root -> Left -> Right
    if not root:
        return
    result = []
    stack = [root]

    while stack:
        current = stack.pop()
        result.append(current.val)
        # Push right first so left is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    print("Binary Tree DFS:", " - ".join(result))


if __name__ == "__main__":
    print("=== BINARY TREE TRAVERSAL (LAAYTADA / LATAYADA) ===")
    root = build_binary_tree()
    bfs(root)
    dfs(root)