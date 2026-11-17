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
        def value(self):
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

    def _adopt_tree(self, other_tree, parent, side):
        node = other_tree._root

        if node is None:
            raise ValueError("Cannot attach an empty tree")

        if side == "left":
            parent.left = node
        else:
            parent.right = node

        node.parent = parent
        other_tree._root = None

    def build_expression_tree(self, expression):
        tokens = expression.split()

        if not tokens:
            raise ValueError("Empty Expression. Invalid Call")
        builder_stack = []
        OPERATOR_SET = {"+", "*", "/", "-"}

        for token in tokens:
            if isinstance(token, (int, float)):
                subtree = BinaryExpressionTree()
                subtree.add_root(token)
                builder_stack.append(subtree)
            elif token in OPERATOR_SET:
                if len(builder_stack) < 2:
                    raise ValueError("Too Few Operands! Invalid Expression")


tree = BinaryExpressionTree()
tree2 = BinaryExpressionTree()
a = tree.add_root("A")
b = tree.add_left(a, "B")
c = tree.add_right(a, "C")
d = tree.add_left(b, "D")

x = tree2.add_root("X")
q = tree2.add_left(x, "Q")

tree2._adopt_tree(tree, tree2._root, "right")

print(tree2.root().value())
print(tree2.left(x).value())
print(tree2.right(x).value())
print(tree2.left(tree2.right(x)).value())
