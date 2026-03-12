from collections import defaultdict, deque
from typing import List, Tuple

"""
Nesse problema iremos receber uma lista de tuplas (pares) que irão conter 2 números inteiros. O primeiro deles
representará um curso e o segundo representará um curso que é pré-requisito para o primeiro curso:

    Exemplo do par: (0, 1) -> Curso 1 é pré-requisito para o curso 0

    Entrada: courses = [(0, 1), (0, 2), (2, 3)]

    O objetivo do algoritmo é retornar um booleano indicando se todos os cursos são
    possíveis de serem feitos dadas as restrições de requisitos.
"""


def is_valid_course_sequence(courses: List[Tuple[int, int]]) -> bool:
    graph = defaultdict(list)
    edges = defaultdict(int)

    # Inicializa todos os cursos no dict edges com grau = 0
    # O(N)
    for dependent, pre_req in courses:
        edges[dependent] = 0
        edges[pre_req] = 0

    # Constrói o Grafo e incrementa o grau de entrada dos nós que são dependentes
    # O(N)
    for dependent, pre_req in courses:
        graph[pre_req].append(dependent)
        edges[dependent] += 1

    # Coloca na fila apenas os nós com grau 0, ou seja, aqueles que não dependem de ninguém
    queue = deque([course for course in edges.keys() if edges[course] == 0])

    sorted_courses = []
    # O(N+M) -> sendo N  a quantidade de nós (cursos) e M a qtd de arestas
    while queue:
        course = queue.popleft()
        sorted_courses.append(course)

        for dependent in graph[course]:
            edges[dependent] -= 1
            if edges[dependent] == 0:
                queue.append(dependent)

    return len(sorted_courses) == len(edges)
