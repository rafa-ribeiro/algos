from typing import List

"""
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix board where board[i][j] = 1 if the ith city and the jth city are 
directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""


def get_number_of_provinces(board: List[List[int]]) -> int:
    """
    Para resolver esse problema precisamos pensar principalmente nos casos em que as cidades são conectadas de forma
    indireta.
    Se quiséssemos identificar uma província somente por cidades que são conectadas diretamente, a abordagem
    usada no Number of Islands funcionaria aqui, mas como uma província é dada por cidades conectadas direta e
    indiretamente precisamos identificar esse segundo caso também

    Uma forma de fazermos isso é mantendo um track de todas as cidades que já foram visitadas anteriormente. Para isso
    criamos a lista visit e a inicializamos com False, ela tem tamanho N (que é a quantidade de linhas da matriz -
    como cada linha da matriz representa as relações de uma cidade com as outras,
    N é a quantidade de cidades do nosso grafo). Assim, toda vez que iniciarmos as relações de uma cidade e ela estiver
    com o valor False, indica que estamos visitando a cidade pela primeira vez, então temos o começo de uma nova
    província. Se já a visitamos antes, então vamos para a próxima cidade, pq isso indica que a cidade já foi
    contabilizada como parte de outra província.

    :param board: List[List[int]
    :return: number_of_provinces: int
    """
    n = len(board)
    number_of_provinces = 0
    visit = [False] * n

    for i in range(n):
        if not visit[i]:
            number_of_provinces += 1
            dfs(i, board, visit)

    return number_of_provinces


def dfs(node: int, board: List[List[int]], visit: List[bool]) -> None:
    """
    Algoritmo recursivo para visitar e marcar as cidades que já foram visitadas a partir de uma cidade inicial,
    dada pelo inteiro node.

    :param node: Representa a cidade que está é visitada
    :param board: Matriz das cidades e as suas relações
    :param visit: Estrutura para lembrarmos quando uma cidade já foi visitada ou não, cada índice representa uma cidade
    """
    visit[node] = True

    for i in range(len(board)):
        if board[node][i] == 1 and not visit[i]:
            dfs(node=i, board=board, visit=visit)
