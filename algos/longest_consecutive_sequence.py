from typing import List

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

"""


def get_longest_consecutive(nums: List[int]) -> int:
    """
    Esse problema seria facilmente resolvido se a lista de nums estivesse ordenada. No entanto, para esse problema, ela
    não está ordenada, e ordená-la não é uma opção porque o problema pede que o algoritmo tenha complexidade de tempo
    de O(N) e, qualquer algoritmo de ordenação, deixa a complexidade da resposta em O(N * Log N).

    A solução aqui para resolver em O(N) é para cada um dos números de nums, identificar quem seria o seu consecutivo
    da esquerda e quem seria seu consecutivo da direita e pegar o total de números que ele já tem de seus respectivos
    consecutivos. Caso não exista consecutivos, o valor que representa a soma desses consecutivos é 0, e caso exista,
    o número consecutivo irá retornar a quantiadde de consecutivos que já encontramos dele.

    Ex:
        Para o input [100, 4, 200, 1, 3, 2]:

        - Inicia o for
        -- num = 100
        -- left de 100 -> 99
        -- right de 100 -> 101
        -- Existe 99 em consecutive_map? Não, então o valor de left é 0
        -- Existe 101 em consecutive_map? Não, então o valor de right é 0
        -- Adiciona no dict: consecutive_map[100] = 1

        -- num = 4
        -- left de 4 -> 3
        -- right de 4 -> 5
        -- Existe 3 em consecutive_map? Não, então o valor de left é 0
        -- Existe 5 em consecutive_map? Não, então o valor de right é 0
        -- Adiciona no dict: consecutive_map[4] = 1

        -- num = 200
        -- left de 200 -> 199
        -- right de 200 -> 201
        -- Existe 199 em consecutive_map? Não, então o valor de left é 0
        -- Existe 201 em consecutive_map? Não, então o valor de right é 0
        -- Adiciona no dict: consecutive_map[200] = 1

        -- num = 1
        -- left de 1 -> 0
        -- right de 1 -> 2
        -- Existe 0 em consecutive_map? Não, então o valor de left é 0
        -- Existe 2 em consecutive_map? Não, então o valor de right é 0
        -- Adiciona no dict: consecutive_map[1] = 1

        -- num = 3
        -- left de 3 -> 2
        -- right de 3 -> 4
        -- Existe 2 em consecutive_map? Não, então o valor de left é 0
        -- Existe 4 em consecutive_map? SIM, então o valor de right é 1
        -- Adiciona no dict: consecutive_map[3] = 2

        -- num = 2
        -- left de 2 -> 1
        -- right de 2 -> 3
        -- Existe 1 em consecutive_map? SIM, então o valor de left é 1
        -- Existe 3 em consecutive_map? SIM, então o valor de right é 2
        -- Adiciona no dict: consecutive_map[2] = 1 + 1 + 2 = 4

    :param nums: List[int]
    :return: max_consecutive: int

    """
    consecutive_map = {}
    max_consecutive = 0
    for num in nums:
        if num not in consecutive_map:
            left = consecutive_map.get(num - 1, 0)
            right = consecutive_map.get(num + 1, 0)

            total = left + 1 + right
            consecutive_map[num] = total

            if total > max_consecutive:
                max_consecutive = total

            consecutive_map[num - left] = total
            consecutive_map[num + right] = total

    return max_consecutive
