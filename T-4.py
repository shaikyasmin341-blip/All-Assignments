#Task Description #4 – Binary Search Tree (BST)
#ask: Ask AI to generate a simple BST with insert() and inorder_traversal().

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def inorder_traversal(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, node):
        res = []
        if node:
            res = self._inorder_rec(node.left)
            res.append(node.val)
            res = res + self._inorder_rec(node.right)
        return res

# Example usage:
if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("Inorder traversal of the BST:", bst.inorder_traversal())