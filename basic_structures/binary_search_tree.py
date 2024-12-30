class BinarySearchTree:
    class Node:
        def __init__(self, val):
            self.data = val
            self.left = None
            self.right = None

    class BSTree:
        def __init__(self):
            self.root = None

        def insert(self, val):
            def _insert(node, val):
                if node is None:
                    return BinarySearchTree.Node(val)
                if val < node.data:
                    node.left = _insert(node.left, val)
                if val > node.data:
                    node.right = _insert(node.right, val)
                return node

            self.root = _insert(self.root, val)

        def DFT(self, node):
            if node is None:
                return
            self.DFT(node.left)
            print(node.data)
            self.DFT(node.right)

        def minimum(self, node):
            if node.left is None:
                return node
            return self.minimum(node.left)

        def delete(self, val):
            def _delete(node, val):
                if node is None:
                    return None

                if val < node.data:
                    node.left = _delete(node.left, val)
                elif val > node.data:
                    node.right = _delete(node.right, val)
                else:
                    nonlocal found
                    found = True
                    if node.left is None:
                        return node.right
                    elif node.right is None:
                        return node.left
                    min_right_node = self.minimum(node.right)
                    node.data = min_right_node.data
                    node.right = _delete(node.right, min_right_node.data)
                return node

            found = False
            self.root = _delete(self.root, val)
            if not found:
                raise KeyError

        # merging two trees
        def merge(self, bstree):
            def _insert(node):
                if node:
                    self.insert(node.data)
                    _insert(node.left)
                    _insert(node.right)

            _insert(bstree.root)
