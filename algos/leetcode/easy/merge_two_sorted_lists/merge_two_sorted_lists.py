from typing import Optional

from dsa.linked_list import ListNode


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2

    if not list2:
        return list1

    if list1.value <= list2.value:
        merged_list = list1
        list1 = list1.next
    else:
        merged_list = list2
        list2 = list2.next

    curr_node = merged_list
    while list1 and list2:
        if list1.value <= list2.value:
            curr_node.next = list1
            list1 = list1.next
        else:
            curr_node.next = list2
            list2 = list2.next

        curr_node = curr_node.next

    if list1 is None:
        curr_node.next = list2
    else:
        curr_node.next = list1

    return merged_list