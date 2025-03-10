from taller_venmo.my_code import my_func
import pytest



@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        (10, 4, 14),
        (99, 1, 100),
    ]
)
def test__my_func(a: int, b: int, expected_result: int):
    result =  my_func(a=a, b=b)
    assert result == expected_result
