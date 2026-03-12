from collections import deque

from dsa.linked_list import ListNode


def is_palindromic_linked_list(head: ListNode | None) -> bool:
    if not head:
        return False

    slow = fast = head
    stack = deque()
    while fast and fast.next:
        stack.append(slow)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    right = slow
    while right:
        left = stack.pop()
        if left.value != right.value:
            return False

        right = right.next

    return True
