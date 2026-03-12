from typing import List
import pytest
from dsa.binary_tree import BinaryNode
from algos.binary_tree_level_order_traversal import list_binary_tree_level_order_traversal_recursive, \
    list_binary_tree_level_order_traversal

root_case_1 = BinaryNode(value=3)
node_9 = BinaryNode(value=9)
node_20 = BinaryNode(value=20)
root_case_1.left = node_9
root_case_1.right = node_20
node_9.left = BinaryNode(value=4)
node_20.left = BinaryNode(value=15)
node_20.right = BinaryNode(value=7)

root_case_2 = BinaryNode(value=99)

root_case_3 = BinaryNode(value=5)
left_rc_3 = BinaryNode(value=10)
right_rc_3 = BinaryNode(value=13)

root_case_3.left = left_rc_3
root_case_3.right = right_rc_3

left_rc_3.left = BinaryNode(value=7)
left_rc_3.right = BinaryNode(value=14)

right_rc_3.left = BinaryNode(value=20)
right_rc_3.right = BinaryNode(value=25)


@pytest.mark.parametrize(
    "node, expected_order",
    [
        (root_case_1, [[3], [9, 20], [4, 15, 7]]),
        (root_case_2, [[99]]),
        (root_case_3, [[5], [10, 13], [7, 14, 20, 25]],)
    ]
)
def test__binary_tree_level_order_traversal(node: BinaryNode, expected_order: List[List]):
    recursive_result = list_binary_tree_level_order_traversal_recursive(node=node)
    assert recursive_result == expected_order

    result = list_binary_tree_level_order_traversal(node=node)
    assert result == expected_order
