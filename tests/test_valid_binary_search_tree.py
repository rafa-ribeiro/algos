import pytest

from algos.valid_binary_search_tree import is_valid_binary_search_tree, is_valid_binary_search_tree_v2
from dsa.binary_tree import BinaryNode

# Case 1
root_c1 = BinaryNode(value=5)
left_r = BinaryNode(value=2)
right_r = BinaryNode(value=10)
root_c1.left = left_r
root_c1.right = right_r
left_r.left = BinaryNode(value=1)
left_r.right = BinaryNode(value=6)

# Case 2
root_c2 = BinaryNode(value=5)
left_r2 = BinaryNode(value=2)
right_r2 = BinaryNode(value=10)

root_c2.left = left_r2
root_c2.right = right_r2

left_r2.left = BinaryNode(value=1)
left_r2.right = BinaryNode(value=3)

node_7 = BinaryNode(value=7)
node_12 = BinaryNode(value=12)
right_r2.left = node_7
right_r2.right = node_12

node_7.left = BinaryNode(value=4)
node_7.right = BinaryNode(value=9)

node_12.left = BinaryNode(value=8)
node_12.right = BinaryNode(value=14)

# Case 3
root_c3 = BinaryNode(value=2)
root_c3.left = BinaryNode(value=1)
root_c3.right = BinaryNode(value=3)

# Case 4
root_c4 = BinaryNode(value=5)
root_c4.left = BinaryNode(value=5)
root_c4.right = BinaryNode(value=5)


@pytest.mark.parametrize(
    "root, expected_result",
    [
        (root_c1, False),
        (root_c2, False),
        (root_c3, True),
        (root_c4, False),
    ]
)
def test__is_valid_binary_search_tree(root, expected_result):
    assert is_valid_binary_search_tree(root) == expected_result


@pytest.mark.parametrize(
    "root, expected_result",
    [
        (root_c1, False),
        (root_c2, False),
        (root_c3, True),
        (root_c4, False),
    ]
)
def test__is_valid_binary_search_tree_v2(root, expected_result):
    assert is_valid_binary_search_tree_v2(root) == expected_result
