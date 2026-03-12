from typing import List
"""



"""


def get_number_of_islands(grid: List[List[str]]) -> int:
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                islands += 1
                expand(grid, i, j)

    return islands


def expand(grid: List[List[str]], i: int, j: int):
    if i < 0 or i > len(grid) - 1:
        return None

    if j < 0 or j > len(grid[0]) - 1:
        return None

    if grid[i][j] == '0' or grid[i][j] == 'V':
        return None

    grid[i][j] = 'V'

    expand(grid, i + 1, j)
    expand(grid, i - 1, j)
    expand(grid, i, j + 1)
    expand(grid, i, j - 1)
