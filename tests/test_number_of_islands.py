import pytest
from typing import List

from algos.number_of_islands import get_number_of_islands

GRID_1 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]

GRID_2 = [
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '0', '0'],
]

GRID_3 = [
    ['0', '0', '0', '0', '0'],
    ['0', '1', '1', '1', '0'],
    ['0', '1', '1', '1', '0'],
    ['0', '0', '0', '0', '0'],
]

GRID_4 = [
    ['1', '0', '1', '0', '1'],
    ['0', '1', '0', '1', '0'],
    ['1', '0', '1', '0', '1'],
    ['0', '1', '0', '1', '0'],
]

GRID_5 = [
    ['1', '1', '1', '1'],
    ['1', '1', '1', '1'],
    ['1', '1', '1', '1'],
    ['1', '1', '1', '1'],
    ['1', '1', '1', '1'],
    ['1', '1', '1', '1'],
]

GRID_6 = [
    ['0', '0', '0', '0'],
    ['0', '0', '0', '0'],
    ['0', '0', '0', '0'],
]


@pytest.mark.parametrize(
    "grid, expected_islands",
    [
        (GRID_1, 3),
        (GRID_2, 1),
        (GRID_3, 1),
        (GRID_4, 10),
        (GRID_5, 1),
        (GRID_6, 0),
    ]
)
def test__get_number_of_islands(grid: List[List[str]], expected_islands: int):
    result = get_number_of_islands(grid=grid)

    assert result == expected_islands
