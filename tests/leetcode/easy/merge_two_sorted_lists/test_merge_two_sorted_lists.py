import pytest

from algos.leetcode.easy.merge_two_sorted_lists.merge_two_sorted_lists import merge_two_lists
from dsa.linked_list import build_linked_list


@pytest.mark.parametrize(
    "head_a, head_b, expected_head",
    [
        (build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4]), build_linked_list([1, 1, 2, 3, 4, 4])),
        (build_linked_list([1, 2, 4]), None, build_linked_list([1, 2, 4])),
        (None, build_linked_list([2]), build_linked_list([2])),
        (build_linked_list([5]), build_linked_list([1, 3, 4, 7, 8, 9]), build_linked_list([1, 3, 4, 5, 7, 8, 9])),
    ]
)
def test__merge_two_sorted_lists(head_a, head_b, expected_head):
    merged_head = merge_two_lists(list1=head_a, list2=head_b)

    while merged_head and expected_head:
        assert merged_head.value == expected_head.value
        merged_head = merged_head.next
        expected_head = expected_head.next


@pytest.mark.parametrize(
    "head_a, head_b, expected_head",
    [
        (None, None, None),
        (build_linked_list([]), build_linked_list([]), build_linked_list([])),
    ]
)
def test__merge_two_sorted_lists_with_empty_lists(head_a, head_b, expected_head):
    merged_head = merge_two_lists(list1=head_a, list2=head_b)

    assert merged_head == expected_head