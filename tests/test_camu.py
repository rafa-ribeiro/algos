from algos.spell_number import spell
import pytest


@pytest.mark.parametrize(
    "number, expected_result",
    [
        (1000, "mil"),
        (100, "cem"),
        (21, "vinte e um"),
        (250, "duzentos e cinquenta"),
        (961, "novecentos e sessenta e um"),
        (197, "cento e noventa e sete"),
        (201, "duzentos e um"),
        (3000, "três mil"),
        (3100, "três mil e cem"),
        (3111, "três mil cento e onze"),
        (3001, "três mil e um"),
        (7054, "sete mil e cinquenta e quatro"),
        (9999, "nove mil novecentos e noventa e nove"),
        (6050, "seis mil e cinquenta"),
        (5010, "cinco mil e dez"),
        (1234, "mil duzentos e trinta e quatro"),
        (1, "um")
    ]
)
def test__spell(number, expected_result):
    result = spell(n=number)

    assert result == expected_result
