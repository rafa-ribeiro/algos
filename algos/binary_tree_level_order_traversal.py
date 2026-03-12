from typing import List
from dsa.binary_tree import BinaryNode
from collections import deque, namedtuple


def list_binary_tree_level_order_traversal_recursive(node: BinaryNode) -> List[List]:
    order = []
    traverse(node=node, order=order)
    return order


def traverse(node: BinaryNode, order: List[List], level=0) -> None:
    if node:
        if level > len(order) - 1:
            order.append([])

        order[level].append(node.value)

        traverse(node.left, order, level + 1)
        traverse(node.right, order, level + 1)


NodeLevel = namedtuple("NodeLevel", "node, level")


def list_binary_tree_level_order_traversal(node: BinaryNode) -> List[List]:
    order = []

    queue = deque()
    queue.append(NodeLevel(node=node, level=0))

    while queue:
        curr_node_level = queue.popleft()
        curr_node = curr_node_level.node
        curr_level = curr_node_level.level

        if curr_node is None:
            continue

        if curr_level > len(order) - 1:
            order.append([])

        order[curr_level].append(curr_node.value)

        queue.append(NodeLevel(node=curr_node.left, level=curr_level + 1))
        queue.append(NodeLevel(node=curr_node.right, level=curr_level + 1))

    return order
