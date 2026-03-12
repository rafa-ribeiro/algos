from typing import List

"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell
or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid
in any number of moves.

"""


def calculate_num_of_enclaves(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])

    rows = [0, n - 1]
    # O(2*M) -> O(M)
    for i in rows:
        for j in range(m):
            if grid[i][j] == 1:
                expand(grid, i, j)

    cols = [0, m - 1]
    # O(2*N) -> O(N)
    for j in cols:
        for i in range(n):
            if grid[i][j] == 1:
                expand(grid, i, j)

    total_moves = 0
    # O(N*M)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 1:
                total_moves += 1

    return total_moves


def expand(grid: List[List[int]], i: int, j: int):
    n = len(grid)
    m = len(grid[0])

    if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or grid[i][j] == -1:
        return

    grid[i][j] = -1

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for row_offset, col_offset in directions:
        expand(grid, i + row_offset, j + col_offset)
