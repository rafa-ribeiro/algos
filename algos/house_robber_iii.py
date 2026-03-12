from typing import Dict, List

from dsa.binary_tree import BinaryNode

"""

House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that all houses in this place form a binary tree.
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

"""


def calculate_max_robbed_amount(root: BinaryNode) -> int:
    dp = dict()
    max_robbed_amount = rob(node=root, dp=dp)
    return max_robbed_amount


def rob(node: BinaryNode | None, dp: Dict[BinaryNode, List], is_parent_robbed=False):
    if not node:
        return 0

    if node not in dp:
        dp[node] = [0, 0]

    idx_case = 1 if is_parent_robbed else 0

    if dp[node][idx_case]:
        # Se já calculamos o valor do roubo para esse nó e no idx_case, apenas retornamos o já calculado
        return dp[node][idx_case]

    # Caso 1: Se o anterior ao nó atual não foi roubado antes, nós podemos roubar aqui
    case_1 = 0
    if not is_parent_robbed:
        case_1 = node.value + rob(node.left, dp, True) + rob(node.right, dp, True)

    # Caso 2: Não roubamos o nó corrent e exploramos os nós abaixo
    case_2 = rob(node.left, dp, False) + rob(node.right, dp, False)

    best_case = max(case_1, case_2)
    dp[node][idx_case] = best_case
    return best_case
