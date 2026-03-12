import pytest

from algos.kth_smallest_element import get_kth_smallest_element_recursive, build_list_from_root_in_order, \
    get_kth_smallest_element, get_kth_smallest_element_recursive_v2, get_kth_smallest_element_iterative
from dsa.binary_tree import BinaryNode

root = BinaryNode(value=3)
left = BinaryNode(value=1)
left.right = BinaryNode(value=2)

root.left = left
root.right = BinaryNode(value=4)


@pytest.mark.parametrize(
    "node, k, expected_kth_value",
    [
        (root, 1, 1),
        (root, 2, 2),
        (root, 3, 3),
        (root, 4, 4),
        (root, 5, 0),
    ]
)
def test__get_kth_smallest_element_recursive(node, k: int, expected_kth_value: int):
    result = get_kth_smallest_element_recursive(root=node, k=k)
    assert result == expected_kth_value

    result = get_kth_smallest_element_recursive_v2(root=node, k=k)
    assert result == expected_kth_value


@pytest.mark.parametrize(
    "node, k, expected_kth_value",
    [
        (root, 1, 1),
        (root, 2, 2),
        (root, 3, 3),
        (root, 4, 4),
        (root, 5, 0),
    ]
)
def test__get_kth_smallest_element(node, k: int, expected_kth_value: int):
    result = get_kth_smallest_element(root=node, k=k)
    assert result == expected_kth_value

    result = get_kth_smallest_element_iterative(root=node, k=k)
    assert result == expected_kth_value


@pytest.mark.parametrize(
    "node, expected_list",
    [
        (root, [1, 2, 3, 4]),
    ]
)
def test__build_list_from_root(node, expected_list):
    elements = build_list_from_root_in_order(root=node)

    assert len(elements) == len(expected_list)
    assert elements == expected_list
