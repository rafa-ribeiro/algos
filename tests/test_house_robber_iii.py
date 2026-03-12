from typing import List, Any

import pytest

from dsa.binary_tree import build_from_list


@pytest.mark.parametrize(
    "_list, expected_root_value",
    [
        ([4, 1, None, 2, None, 3], 4),
        ([1, 2, 3, 4, 5, 6, 7], 1),
        ([3, 4, 5, 1, 3, None, 1], 3),
        ([3, 4, None, 1, 3, None, 4,1], 3),
        ([3, 2, 3, None, 3, None, 1], 3),
    ]
)
def test__calculate_max_robbed_amount(_list: List[Any], expected_root_value: Any):
    root_node = build_from_list(_list=_list)
    assert root_node.value == expected_root_value
