from typing import List
from collections import deque


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.childs: List[TreeNode] = []

    def append(self, child):
        self.childs.append(child)


def print_tree_bfs(node: TreeNode) -> None:
    queue = deque()
    queue.append(node)

    while queue:
        curr_node = queue.popleft()
        print(curr_node.value, end=" ")

        for child in curr_node.childs:
            queue.append(child)


def print_tree_dfs(node: TreeNode) -> None:
    stack = deque()
    stack.append(node)

    while stack:
        curr_node = stack.pop()
        print(curr_node.value, end=" ")
        for child in curr_node.childs:
            stack.append(child)


def contains_bfs(node: TreeNode, value: str) -> bool:
    queue = deque()
    queue.append(node)

    while queue:
        curr_node = queue.popleft()
        if curr_node.value == value:
            return True

        for child in curr_node.childs:
            queue.append(child)

    return False


def contains_dfs(node: TreeNode, value: str) -> bool:
    stack = deque()
    stack.append(node)

    while stack:
        curr_node = stack.pop()
        if curr_node.value == value:
            return True

        for child in curr_node.childs:
            stack.append(child)

    return False


root = TreeNode(value="1")
node_2 = TreeNode(value="2")
root.append(node_2)
root.append(TreeNode(value="3"))

node_4 = TreeNode(value="4")
root.append(node_4)

node_2.append(TreeNode(value="5"))
node_2.append(TreeNode(value="6"))

node_4.append(TreeNode(value="7"))
node_4.append(TreeNode(value="8"))

print_tree_bfs(node=root)
print()
print_tree_dfs(node=root)

print()
print(contains_bfs(node=root, value="6"))
print(contains_bfs(node=root, value="10"))
print(contains_bfs(node=node_4, value="8"))
print(contains_bfs(node=node_4, value="5"))

print()
print(contains_dfs(node=root, value="6"))
print(contains_dfs(node=root, value="10"))
print(contains_dfs(node=node_4, value="8"))
print(contains_dfs(node=node_4, value="5"))
