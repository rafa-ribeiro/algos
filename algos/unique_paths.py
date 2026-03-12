from typing import List


def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    return find_path(obstacle_grid)


def find_path(grid: List[List[int]]) -> int:
    """
    Algoritmo find_path recursivo com uso de memoization.

    Esse é um exemplo muito legal para estudar Dynamic Programming.

    Na versão simples desse algoritmo, nós sempre verificamos os atuais índices de linha e coluna pra verificar
    se estão em pontos válidos dentro do grid e se seu conteúdo é de um espaço vazio ou obstáculo.

    Assim, é possível identificar que pode haver muitos caminhos que passam pelas mesmas casas no grid até o
    alvo final, e assim, não precisamos efetuar novamente todas as verificações porque já fizemos uma vez, então
    precisamos apenas salvar essa computação de forma com que consiga acessar rapidamente o seu resultado antes
    calculado.
    Para isso, criamos um novo grid em que todos os seus elementos foram inicializados com valor 0, indicando que
    não foi feita computação para esse elemento, e ao calcularmos um valor, nós o substituímos no grid dp.

    :param grid:
    :return:
    """
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0] * cols for _ in range(rows)]

    def solve_path(cur_row, cur_col):
        if cur_row < 0 or cur_col < 0 or cur_row >= rows or cur_col >= cols or grid[cur_row][cur_col]:
            return 0

        if cur_row == rows - 1 and cur_col == cols - 1:
            return 1

        if dp[cur_row][cur_col]:
            return dp[cur_row][cur_col]

        dp[cur_row][cur_col] = solve_path(cur_row + 1, cur_col) + solve_path(cur_row, cur_col + 1)
        return dp[cur_row][cur_col]

    return solve_path(cur_row=0, cur_col=0)
