import unittest
from Stack import Stack
from binary_expression_tree import BinaryExpressionTree


class TestBinaryExpressionTree(unittest.TestCase):

    def setUp(self):
        self.test_stack = Stack()
        self.test_builder_tree = BinaryExpressionTree()
        self.test_expression1 = " 5 4 + 3 * "
        self.test_expression2 = " 5 3 * 2 /"
        self.test_expression3 = " 5 0 /"
        self.test_expression3 = " "

    def test_evaluation1(self):
        self.test_tree = self.test_builder_tree.build_expression_tree(self.test_expression1)
        self.assertEqual(self.test_tree.core_evaluate(), 27.0)

    def test_evaluation2(self):
        self.test_tree = self.test_builder_tree.build_expression_tree(self.test_expression2)
        self.assertEqual(self.test_tree.core_evaluate(), 7.5)


    def test_invalid_evaluation1(self):
        self.test_tree = self.test_builder_tree.build_expression_tree(self.test_expression3)
        with self.assertRaises(ZeroDivisionError):
            self.test_tree.core_evaluate()
    def test_invalid_evaluation2(self):
        self.test_tree = self.test_builder_tree.build_expression_tree(self.test_expression3)
        with self.assertRaises(ZeroDivisionError):
            self.test_tree.core_evaluate()

if __name__ == "__main__":
    unittest.main()