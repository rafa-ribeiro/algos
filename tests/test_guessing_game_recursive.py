import pytest
from algos.guessing_game_recursive import GuessGame

@pytest.mark.parametrize(
    "n, picked",
    [
        (3, 2),
        (1000, 50),
        (10, 6),
        (1, 1),
        (2, 1),
    ]
)
def test__guessing_game_recursive(n: int, picked: int,):
    guess_game = GuessGame(picked=picked)

    result = guess_game.guessNumber(n=n)
    assert result == picked
