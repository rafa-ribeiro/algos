from typing import List

from dsa.binary_tree import BinaryNode


def get_kth_smallest_element_recursive(root: BinaryNode, k: int) -> int:
    """
    Time = O(N)
    Space = O(N) Devido as chamadas recursivas
    """
    kth = [0]
    kth_element: List[BinaryNode | None] = [None]

    def _get_kth(node: BinaryNode | None):
        if not node or kth[0] > k:
            return

        _get_kth(node=node.left)
        kth[0] += 1

        if kth[0] == k:
            kth_element[0] = node
            return

        _get_kth(node=node.right)

    _get_kth(node=root)
    return kth_element[0].value if kth_element[0] else 0


def get_kth_smallest_element_recursive_v2(root: BinaryNode, k: int) -> int:
    def _get_kth(node: BinaryNode | None, count: int) -> tuple[int, BinaryNode | None]:
        if not node:
            return count, None

        # Visita a subárvore esquerda
        count, result = _get_kth(node.left, count)
        if result:  # Se o k-ésimo elemento já foi encontrado, retorne
            return count, result

        # Visita o nó atual
        count += 1
        if count == k:
            return count, node

        # Visita a subárvore direita
        return _get_kth(node.right, count)

    _, result_node = _get_kth(root, 0)
    return result_node.value if result_node else 0


def get_kth_smallest_element(root: BinaryNode, k: int) -> int:
    """
    Complexity = O(N)
    Space = O(N)
    """
    elements = build_list_from_root_in_order(root=root)
    if k > len(elements):
        return 0

    return elements[k - 1]


def build_list_from_root_in_order(root: BinaryNode) -> List[int]:
    """
    Usando In-Order traversal algorithm
    """
    elements = []

    def _populate(node: BinaryNode) -> None:
        if not node:
            return

        _populate(node.left)
        elements.append(node.value)
        _populate(node.right)

    _populate(node=root)
    return elements


def get_kth_smallest_element_iterative(root: BinaryNode, k: int) -> int:
    """
    Complexity:
    - Time = O(N)
    - Space = O(h) -> Sendo h a altura da árvore
    """
    stack = []
    curr_node = root
    count = 0

    while stack or curr_node:
        # Visita todos os nós à esquerda
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left

        # Visita o nó atual
        curr_node = stack.pop()
        count += 1
        if count == k:
            return curr_node.value

        # Visita a subárvore direita
        curr_node = curr_node.right

    return 0  # Se o k-ésimo elemento não for encontrado