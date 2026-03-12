from typing import List

import pytest

from algos.longest_consecutive_sequence import get_longest_consecutive


@pytest.mark.parametrize(
    "nums, expected_longest_sequence",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3], 5),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
        ([1, 3, 5], 1),
        ([1, 3, 5, 7, 8], 2),
    ]
)
def test__get_longest_consecutive_sequence(nums: List[int], expected_longest_sequence: int):
    result = get_longest_consecutive(nums=nums)
    assert result == expected_longest_sequence
