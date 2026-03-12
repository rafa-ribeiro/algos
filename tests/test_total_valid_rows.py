from typing import List
import pytest
from algos.total_valid_rows import count_valid_rows


@pytest.mark.parametrize(
    "relations_row, expected_total_rows",
    [
        (["A > B", "B > C", "A > C"], 1),
        (["A>B", "A>C"], 2),
        (["A>B", "A<C", "C<Z"], 1),
        (["A>B", "B<A"], 1),
        (["A>B", "B>A"], 0),
        (["A>B", "C>D"], 6),
    ]
)
def test__count_valid_rows(relations_row: List[str], expected_total_rows):
    assert count_valid_rows(relations_row=relations_row) == expected_total_rows
