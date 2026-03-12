from typing import List, Any

import pytest

from algos.palindrome_in_linked_list import is_palindromic_linked_list
from dsa.linked_list import build_linked_list


@pytest.mark.parametrize(
    "_list, is_palindrome",
    [
        ([1, 2, 3], False),
        ([5, 4, 3, 4, 5], True),
        ([5, 4, 3, 3, 4, 5], True),
        ([5, 4, 3, 3, 7, 5], False),
        ([1, 2, 3, 4, 3, 2, 1], True),
        ([1, 2, 3, 4, 4, 3, 2, 1], True),
        ([], False),
        ([5], True),
        ([5, 5], True),
        ([1, 5, 1], True),
    ]
)
def test__is_palindromic_linked_list(_list: List[Any], is_palindrome: bool):
    list_node = build_linked_list(_list=_list)

    result = is_palindromic_linked_list(head=list_node)
    assert result == is_palindrome
