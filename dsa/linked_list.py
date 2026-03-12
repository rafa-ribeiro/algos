from typing import Any, List


class ListNode:

    def __init__(self, value: Any):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node(value={self.value}, next={self.next.value if self.next else 'None'})"


def build_linked_list(_list: List[Any]) -> ListNode | None:
    if not _list:
        return None

    head = ListNode(value=_list[0])
    prev_node = head
    for item in _list[1:]:
        next_node = ListNode(value=item)
        prev_node.next = next_node
        prev_node = next_node

    return head


def convert_to_list(head: ListNode) -> List[Any]:
    _list = []
    while head:
        _list.append(head.value)
        head = head.next

    return _list


def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr:
        _next = curr.next # salva o next para não perdermos a referência
        curr.next = prev # o curr passa a apontar para o prev
        prev = curr # o curr passa a ser o anterior, prev vai conter o último elemento da lista que será a nova head
        curr = _next  # o next passa a ser o curr

    return prev
