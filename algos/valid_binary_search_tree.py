import sys

from dsa.binary_tree import BinaryNode

MAX_VALUE = sys.maxsize
MIN_VALUE = -sys.maxsize - 1


def is_valid_binary_search_tree(root: BinaryNode) -> bool:
    is_left_valid = _is_valid_node(node=root.left, start=MIN_VALUE, end=root.value - 1)
    is_right_valid = _is_valid_node(node=root.right, start=root.value + 1, end=MAX_VALUE)
    return is_left_valid and is_right_valid


def _is_valid_node(node: BinaryNode, start: int, end: int) -> bool:
    if not node:
        return True

    if node.value > end or node.value < start:
        return False

    is_left_valid = _is_valid_node(node=node.left, start=start, end=node.value - 1)
    is_right_valid = _is_valid_node(node=node.right, start=node.value + 1, end=end)

    return is_left_valid and is_right_valid


def is_valid_binary_search_tree_v2(root: BinaryNode) -> bool:
    return is_valid_node_v2(node=root, start=MIN_VALUE, end=MAX_VALUE)


def is_valid_node_v2(node: BinaryNode, start: int, end: int) -> bool:
    if not node:
        return True

    if node.value > end or node.value < start:
        return False

    is_left_valid = _is_valid_node(node=node.left, start=start, end=node.value - 1)
    is_right_valid = _is_valid_node(node=node.right, start=node.value + 1, end=end)

    return is_left_valid and is_right_valid
