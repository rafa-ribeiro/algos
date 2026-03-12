from collections import deque
from typing import Any, List


class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left: BinaryNode | None = None
        self.right: BinaryNode | None = None

    def __str__(self):
        return f"BinaryNode(value={self.value}, left={self.left.value if self.left else 'None'}, right={self.right.value if self.right else 'None'})"


def build_from_list(_list: List[Any]):
    if not _list:
        return None

    all_nodes = deque()
    for item in _list:
        all_nodes.append(BinaryNode(value=item) if item else None)

    _root = all_nodes.popleft()
    parent_nodes = deque()
    parent_nodes.append(_root)

    while all_nodes:
        curr = parent_nodes.popleft()
        if not curr:
            continue

        left = all_nodes.popleft()
        right = all_nodes.popleft() if all_nodes else None
        curr.left = left
        curr.right = right
        parent_nodes.append(left)
        parent_nodes.append(right)

    return _root


def print_pre_order(node: BinaryNode) -> None:
    if node is None:
        return None

    print(node.value, end=" ")
    print_pre_order(node=node.left)
    print_pre_order(node=node.right)


def print_pre_order_iterative(node: BinaryNode) -> None:
    stack = deque()

    if node:
        stack.append(node)

    while stack:
        curr_node = stack.pop()
        print(curr_node.value, end=" ")
        stack.append(curr_node.right) if curr_node.right else ...  # Colocamos na pilha o lado direito
        stack.append(curr_node.left) if curr_node.left else ...
        # E depois o esquerdo, para a impressão do esquerdo ocorrer antes do direito


def print_pre_order_iterative_v2(node: BinaryNode) -> None:
    stack = deque()

    if node:
        stack.append(node)

    curr_node = None
    while stack:
        if curr_node is None:
            curr_node = stack.pop()

        print(curr_node.value, end=" ")
        stack.append(curr_node.right) if curr_node.right else ...  # Colocamos na pilha o lado direito
        curr_node = curr_node.left


def print_post_order(node: BinaryNode) -> None:
    if node is None:
        return None

    print_post_order(node=node.left)
    print_post_order(node=node.right)
    print(node.value, end=" ")


def print_post_order_no_recursion(node: BinaryNode) -> None:
    stack_visited = deque()  # Pilha para indicar os nós visitados
    stack_order = deque()  # Pilha contendo a ordem de impressão de cada nó, o topo primeiro

    if node:
        stack_visited.append(node)

    while stack_visited:
        curr_node = stack_visited.pop()
        stack_order.append(curr_node)

        stack_visited.append(curr_node.left) if curr_node.left else ...
        stack_visited.append(curr_node.right) if curr_node.right else ...

    while stack_order:
        print(stack_order.pop().value, end=" ")


def print_in_order(node: BinaryNode) -> None:
    if node is None:
        return None

    print_in_order(node=node.left)
    print(node.value, end=" ")
    print_in_order(node=node.right)


def print_in_order_no_recursion(node: BinaryNode) -> None:
    stack = deque()
    curr_node = node
    while curr_node or stack:
        if curr_node:
            stack.append(curr_node)  # Adiciona o nó atual na pilha
            curr_node = curr_node.left  # Caminha para a esquerda
        elif stack:  # Se curr_node é vazio é porque chegamos numa folha
            curr_node = stack.pop()  # Então o nó corrente é retirado da stack
            print(curr_node.value, end=" ")  # Imprimimos o valor
            curr_node = curr_node.right  # Caminhamos para a direita, reinicia o fluxo indo para a esquerda até encontrar outra folha


root = BinaryNode(value="1")
node_2 = BinaryNode(value="2")
node_3 = BinaryNode(value="3")

root.left = node_2
root.right = node_3

node_2.left = BinaryNode(value="4")
node_2.right = BinaryNode(value="5")

node_3.left = BinaryNode(value="6")
node_3.right = BinaryNode(value="7")

print("\nPre Order: ")
print_pre_order(node=root)

print("\nPre Order (no recursion): ")
print_pre_order_iterative(node=root)

print("\nPre Order (no recursion V2): ")
print_pre_order_iterative_v2(node=root)

print("\nPost Order: ")
print_post_order(node=root)

print("\nPost Order (no recursion): ")
print_post_order_no_recursion(node=root)

print("\nIn Order: ")
print_in_order(node=root)

print("\nIn Order (no recursion): ")
print_in_order_no_recursion(node=root)
