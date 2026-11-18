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
            raise ValueError("Empty Expression. Invalid Call!")
        builder_stack = []
        OPERATOR_SET = {"+", "*", "/", "-"}

        for token in tokens:
            try:
                number = float(token)
                subtree = BinaryExpressionTree()
                subtree.add_root(token)
                builder_stack.append(subtree)
                continue
            except ValueError:
                pass 

            if token in OPERATOR_SET:
                if len(builder_stack) < 2:
                    raise ValueError("Too Few Operands. Invalid Expression!")
                right_subtree = builder_stack.pop()
                left_subtree = builder_stack.pop()

                subtree = BinaryExpressionTree()
                subtree.add_root(token)
                subtree._adopt_tree(left_subtree, subtree._root, "left")
                subtree._adopt_tree(right_subtree, subtree._root, "right")

                builder_stack.append(subtree)
            else:
                print(f"Invalid token: {token}")
                raise ValueError("Invalid Token!")

        if len(builder_stack) != 1:
            raise ValueError("Uhm, somehow you don't have a single expression tree. Invalid Expression!")

        return builder_stack.pop()


    def core_evaluate(self):
        if self._root is None:
            raise ValueError("Empty Tree. Invalid!")
        return self._recursive_evaluate(self._root)

    def _recursive_evaluate(self, node): #ew, but yay!
        if node.left is None and node.right is None:
            return float(node.value)

        if node.left is None or node.right is None:
            raise ValueError("Operator must have two children")

        left_value = self._recursive_evaluate(node.left)
        right_value = self._recursive_evaluate(node.right)

        if node.value == "+":
            return left_value + right_value
        elif node.value == "-":
            return left_value - right_value
        elif node.value == "*":
            return left_value * right_value
        elif node.value == "/":
            if right_value == 0:
                raise ZeroDivisionError
            return left_value / right_value
        else:
            raise ValueError("Unsupported Operator")


