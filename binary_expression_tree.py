from Stack import Stack

class BinaryExpressionTree:
    class _Node:
        def __init__(self, value, parent=None):
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
    
    def node_value(self):
        return self._node.value
    def __init__(self):
        self._root = None
    def _make_position(self, node):
        if node:
            return self.Position(self, node)
        else:
            return None
    def _validate(self, p):
        if not isinstance(p, self.Position) or p._container is not self:
            raise ValueError("Position does not belong to this tree")
        return p._node
    def root(self):
        return self._make_position(self._root)
    def parent(self, p):
        return self._make_position(self._validate(p).parent)
    def left(self, p):
        return self._make_position(self._validate(p).left)
    def right(self, p):
        return self._make_position(self._validate(p).right)
    def is_leaf(self, p):
        node = self._validate(p)
        return node.left is None and node.right is None
    def add_root(self, e):
        if self._root is not None:
            raise ValueError("Tree already has a root")
        self._root = self._Node(e)
        return self.root()
    def add_left(self, p, e):
        node = self._validate(p)
        if node.left is not None:
            raise ValueError("Left child already exists")
        node.left = self._Node(e, node)
        return self._make_position(node.left)
    def add_right(self, p, e):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError("Right child already exists")
        node.right = self._Node(e, node)
        return self._make_position(node.right)
