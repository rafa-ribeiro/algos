import pytest

from algos.number_of_provinces import get_number_of_provinces


@pytest.mark.parametrize(
    "board, expected_provinces",
    [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1),
        ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 1),
        ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4),
    ]
)
def test__number_of_provinces(board, expected_provinces):
    result = get_number_of_provinces(board=board)
    assert result == expected_provinces
