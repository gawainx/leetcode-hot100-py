from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        visited = [[False for _ in range(width)] for _ in range(height)]
        num_island = 0
        for i in range(height):
            for j in range(width):
                if visited[i][j]:
                    continue
                if grid[i][j] == "1":
                    search_stack = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
                    while len(search_stack) > 0:
                        next_i, next_j = search_stack.pop()
                        if next_j >= width or next_i >= height:
                            continue
                        if next_j < 0 or next_i < 0:
                            continue
                        if visited[next_i][next_j]:
                            continue
                        if grid[next_i][next_j] == "1":
                            search_stack.append((next_i + 1, next_j))
                            search_stack.append((next_i - 1, next_j))
                            search_stack.append((next_i, next_j + 1))
                            search_stack.append((next_i, next_j - 1))
                        visited[next_i][next_j] = True
                    num_island += 1

                visited[i][j] = True
        return num_island
