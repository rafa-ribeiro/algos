import pytest

from algos.minimum_depth_binary_tree import get_minimum_depth_binary_tree, get_minimum_depth_binary_tree_recursive
from dsa.binary_tree import BinaryNode

# Case 1
root_c1 = BinaryNode(value=3)
root_c1.left = BinaryNode(value=9)
right_c1 = BinaryNode(value=20)

root_c1.right = right_c1

right_c1.left = BinaryNode(value=15)
right_c1.right = BinaryNode(value=7)

# Case 2
root_c2 = BinaryNode(value=3)
left_c2 = BinaryNode(value=9)
root_c2.left = left_c2
root_c2.right = BinaryNode(value=20)

left_c2.left = BinaryNode(value=1)
left_c2.right = BinaryNode(value=3)

root_c3 = BinaryNode(value=2)
right_c3 = BinaryNode(value=3)
root_c3.right = right_c3

node_4 = BinaryNode(value=4)
right_c3.right = node_4

node_4.right = BinaryNode(value=5)


@pytest.mark.parametrize(
    "root, expected_depth",
    [
        (root_c1, 2),
        (root_c2, 2),
        (root_c3, 4),
        (BinaryNode(value=1), 1),
        (None, 0),
    ]
)
def test__get_minimum_depth_binary_tree(root: BinaryNode, expected_depth):
    result = get_minimum_depth_binary_tree(root=root)
    assert result == expected_depth

    res = get_minimum_depth_binary_tree_recursive(root=root)
    assert res == expected_depth
