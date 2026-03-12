import pytest
from algos.quicksort import quicksort


@pytest.mark.parametrize(
    "items, expected_ordered_items",
    [
        ([], []),
        ([3], [3]),
        ([1, 3, 2], [1, 2, 3]),
        ([8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17], [3, 5, 7, 8, 12, 17, 25, 29, 35, 41, 44, 55, 82]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),

    ]
)
def test__quicksort(items, expected_ordered_items):
    ordered_items = quicksort(items=items)

    assert ordered_items == expected_ordered_items
