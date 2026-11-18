from binary_expression_tree import BinaryExpressionTree

useful_expression = " 5 4 * 7 3 + * "
intermediary = BinaryExpressionTree()
final_tree = intermediary.build_expression_tree(useful_expression)

print(f"The Original Expression: {useful_expression}")
print(f"The Infix-Converted Expression: {final_tree.core_infix_converter()}")
print(f"The Postfix-Converted Expression: {final_tree.core_postfix_converter()}")
print(f"The Evaluated Expression: {final_tree.core_evaluate()}")
print()