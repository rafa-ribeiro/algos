from typing import List

import pytest

from algos.number_of_enclaves import calculate_num_of_enclaves


@pytest.mark.parametrize(
    "grid, expected_num_of_enclaves",
    [
        ([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 3),
        ([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], 0),
        ([[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 0),
        ([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], 1),
        ([[0, 0, 0, 1, 1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
          [0, 1, 1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]], 3),
    ]
)
def test__num_of_enclaves(grid: List[List[int]], expected_num_of_enclaves: int):
    num_of_enclaves = calculate_num_of_enclaves(grid=grid)
    assert num_of_enclaves == expected_num_of_enclaves
