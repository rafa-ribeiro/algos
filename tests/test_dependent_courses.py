from typing import List, Tuple
import pytest
from algos.dependent_courses import is_valid_course_sequence


@pytest.mark.parametrize(
    "courses, expected_result",
    [
        # Caso 1: Ciclo direto (0 -> 1 -> 0) - Não é possível completar os cursos.
        ([(0, 1), (1, 0)], False),

        # Caso 2: Sem ciclos - É possível completar os cursos.
        ([(0, 1), (1, 2)], True),

        # Caso 3: Ciclo indireto (0 -> 1 -> 2 -> 0) - Não é possível completar os cursos.
        ([(0, 1), (1, 2), (2, 0)], False),

        # Caso 4: Sem ciclos, mas com múltiplos pré-requisitos - É possível completar os cursos.
        ([(0, 1), (0, 2), (1, 3), (2, 3)], True),

        # Caso 5: Ciclo em um subgrafo (1 -> 2 -> 3 -> 1) - Não é possível completar os cursos.
        ([(0, 1), (1, 2), (2, 3), (3, 1)], False),

        # Caso 6: Sem ciclos, com múltiplos cursos sem pré-requisitos - É possível completar os cursos.
        ([(1, 0), (2, 0), (3, 1), (3, 2)], True),

        # Caso 7: Grafo desconexo sem ciclos - É possível completar os cursos.
        ([(0, 1), (2, 3)], True),

        # Caso 8: Grafo desconexo com ciclo em um dos subgrafos - Não é possível completar os cursos.
        ([(0, 1), (1, 0), (2, 3)], False),

        # Caso 9: Lista vazia - Não há cursos, então é "vacuamente" possível.
        ([], True),
    ]
)
def test__is_valid_grade(courses: List[Tuple[int, int]], expected_result: bool):
    assert is_valid_course_sequence(courses=courses) == expected_result
