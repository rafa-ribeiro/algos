from typing import List, Any

import pytest

from dsa.linked_list import build_linked_list, convert_to_list, reverse_linked_list


@pytest.mark.parametrize(
    "_list, expected_head_value",
    [
        ([1, 2, 3], 1),
        ([5, 4, 3, 4, 5], 5),
        ([9, 2], 9),
    ]
)
def test__build_linked_list(_list: List[Any], expected_head_value: Any):
    list_node = build_linked_list(_list=_list)

    assert list_node.value == expected_head_value

    node = list_node
    for item in _list:
        assert node.value == item
        node = node.next


@pytest.mark.parametrize(
    "expected_list",
    [
        ([1, 2, 3]),
        ([5, 4, 3, 4, 5]),
        ([9, 2]),
    ]
)
def test__convert_to_list(expected_list):
    head = build_linked_list(_list=expected_list)
    _list = convert_to_list(head=head)

    assert _list == expected_list


@pytest.mark.parametrize(
    "_list, expected_rev_head_value",
    [
        ([1, 2, 3], 3),
        ([5, 4, 3, 4, 5], 5),
        ([9, 2], 2),
        ([1, 2, 3, 4, 5, 6], 6),
    ]
)
def test__reverse_linked_list(_list: List, expected_rev_head_value):
    head = build_linked_list(_list=_list)
    reversed_head = reverse_linked_list(head=head)
    assert reversed_head.value == expected_rev_head_value

    reversed_list = convert_to_list(head=reversed_head)
    assert reversed_list == _list[::-1]
