from typing import List
from collections import defaultdict, deque

"""
Dada uma lista de strings no modelo abaixo. Escreva uma algoritmo que saiba identificar quantas combinações de filas
diferentes são possíveis respeitando a restrição de ordem de chegada:

Input: ["A > B", "B > C", "A > C"]

Nesse exemplo os sinais ">" e "<" indicam quem tem prioridade na fila.

- "A > B" indica que A está na frente de B na fila

Logo, as possíveis formações de fila com esse desenho são:

1 - A, B, C

Assim, o resultado deve ser 1.

"""

def count_valid_rows(relations_row: List[str]) -> int:
    # Criar o grafo a partir das relações entre as pessoas na fila
    graph = defaultdict(list)
    degrees = defaultdict(int)

    # O(N)
    for pair in relations_row:
        if '>' in pair:
            left, right = pair.split(">")
            left, right = left.strip(), right.strip()
            graph[right].append(left)
            degrees[left] += 1
            degrees[right] += 0
        elif '<' in pair:
            left, right = pair.split("<")
            left, right = left.strip(), right.strip()
            graph[left].append(right)
            degrees[right] += 1
            degrees[left] += 0

    total_valid_rows = count_rows(graph=graph, degrees=degrees, current_row=[])
    return total_valid_rows


def count_rows(graph, degrees, current_row):
    if len(current_row) == len(degrees):
        return 1

    # O(N)
    start_nodes = [node for node, degree in degrees.items() if degree == 0 and node not in current_row]

    total_rows = 0
    # O(N * M) -> Sendo N a quantidade de nós e M a quantidade de arestas
    for node in start_nodes:
        # Adiciona o nó na fila corrente
        current_row.append(node)

        for relation in graph[node]:
            degrees[relation] -= 1

        total_rows += count_rows(graph, degrees, current_row)

        # Como estamos iterando o start_node que são sempre nós com grau 0, após contabilizar a row,
        # precisamos restaurar a fila e os graus alterados para o próximo nó grau 0 trabalhar com o dicionário original
        # de graus.
        current_row.pop()
        for relation in graph[node]:
            degrees[relation] += 1

    return total_rows