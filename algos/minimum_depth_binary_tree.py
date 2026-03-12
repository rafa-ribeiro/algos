from collections import deque, namedtuple

from dsa.binary_tree import BinaryNode

NodeLevel = namedtuple("NodeLevel", "node level")


def get_minimum_depth_binary_tree(root: BinaryNode) -> int:
    if not root:
        return 0

    min_depth = 1000

    stack = deque()
    stack.append(NodeLevel(node=root, level=1))
    while stack:
        curr_node_level = stack.pop()
        curr_node = curr_node_level.node
        curr_level = curr_node_level.level

        if not curr_node:
            continue

        is_leaf = curr_node.left is None and curr_node.right is None
        if is_leaf:
            min_depth = min(min_depth, curr_level)
            continue

        if curr_level + 1 < min_depth:
            stack.append(NodeLevel(node=curr_node.left, level=curr_level + 1))
            stack.append(NodeLevel(node=curr_node.right, level=curr_level + 1))

    return min_depth


def get_minimum_depth_binary_tree_recursive(root: BinaryNode) -> int:
    min_depth = [1000 if root else 0]

    def _get_min_depth(node: BinaryNode | None, depth=1):
        if not node:
            return

        is_leaf = node.left is None and node.right is None
        if is_leaf:
            min_depth[0] = min(min_depth[0], depth)
            return

        if depth + 1 < min_depth[0]:
            _get_min_depth(node=node.left, depth=depth + 1)
            _get_min_depth(node=node.right, depth=depth + 1)

    _get_min_depth(node=root)
    return min_depth[0]
