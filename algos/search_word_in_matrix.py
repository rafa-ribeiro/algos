from collections import defaultdict
from typing import List, Tuple, Dict

"""
Dada uma matrix m x n e uma string word, escreva um algoritmo que retorna True se a palavra for encontrada na matriz
e False caso não encontrada. Uma palavra pode ser formada tanto de forma horizontal quanto na vertial ou ambos


"""


def search_word_recursive(board: List[List[str]], word: str) -> bool:
    rows = len(board)
    cols = len(board[0])

    for row in range(rows):
        for col in range(cols):
            if _find_suffix(board=board, suffix=word, row=row, col=col):
                return True

    return False


def _find_suffix(board: List[List[str]], row: int, col: int, suffix: str) -> bool:
    if len(suffix) == 0:
        return True

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != suffix[0]:
        return False

    board[row][col] = '#'

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for row_offset, col_offset in directions:
        if _find_suffix(board=board, row=row + row_offset, col=col + col_offset, suffix=suffix[1:]):
            board[row][col] = suffix[0]
            return True

    return False


def search_word(board: List[List[str]], word: str) -> bool:
    # 1. Varrer a board e encontrar todas as células iguais a primeira letra de word
    # 2. Varrer o board e criar um Dict[str, List[]] que será colocado as letras adjacentes
    # 3. Para cada letra igual a word, iterar no dict, toda vez que encontrar uma letra igual, incrementa o índice da palavra
    # 4. Se a índice for igual ao tamanho de word -1, encontramos a palavra na board
    # 5. Esse loop será executado até encontrarmos a palavra ou até o board acabar

    graph = defaultdict(list)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    all_starts: List[Tuple] = list()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == word[0]:
                all_starts.append((row, col))

            for row_offset, col_offset in directions:
                adj_row = row + row_offset
                adj_col = col + col_offset

                is_valid_cell = 0 <= adj_row < len(board) and 0 <= adj_col < len(board[row])
                if is_valid_cell:
                    graph[board[row][col]].append(board[adj_row][adj_col])

    for row, col in all_starts:
        curr_letter = board[row][col]
        word_idx = 1
        visited = set()

        result = _find_w(board, curr_letter, graph, word_idx, word, visited)
        if result:
            return True

    return False


def _find_w(board: List[List[str]], letter: str, graph: Dict[str, List], count_idx: int, word: str,
            visited: set) -> bool:
    if count_idx == len(word):
        return True

    for adj in graph[letter]:
        if adj == word[count_idx]:
            if _find_w(board, adj, graph, count_idx + 1, word, visited):
                return True

    return False
