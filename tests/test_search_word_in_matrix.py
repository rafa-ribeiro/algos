from typing import List

import pytest
from copy import deepcopy

from algos.search_word_in_matrix import search_word_recursive, search_word

board_1 = [
    ['R', 'A', 'P'],
    ['Y', 'F', 'T'],
    ['I', 'A', 'J'],
    ['R', 'E', 'N'],
    ['A', 'L', 'M'],
]

board_2 = deepcopy(board_1)

@pytest.mark.parametrize(
    "board, word, expected_result",
    [
        (board_1, "RAFA", True),
        (board_1, "RAFAEL", True),
        (board_1, "RYI", True),
        (board_1, "ABC", False),
        (board_1, "REN", True),
        (board_1, "PTJNM", True),
        (board_1, "RAT", False),
    ]
)
def test__search_word_recursive(board: List[List[str]], word: str, expected_result: bool):
    result = search_word_recursive(board=board, word=word)

    assert result == expected_result


@pytest.mark.parametrize(
    "board, word, expected_result",
    [
        (board_2, "RAFA", True),
        (board_2, "RAFAEL", True),
        (board_2, "RAFAELO", False),
        (board_2, "RYI", True),
        (board_2, "ABC", False),
        (board_2, "REN", True),
        (board_2, "PTJNM", True),
        (board_2, "RAT", False),
    ]
)
def test__search_word(board: List[List[str]], word: str, expected_result: bool):
    result = search_word(board=board, word=word)

    assert result == expected_result
