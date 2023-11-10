import collections
from typing import List


class Solution:
    # if arrived
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col, grid):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != "1":
                return

            grid[row][col] = "0"

            directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for r, c in directions:
                dfs(r, c, grid)

        # original grid[row][col] == "1" but near  grid[row][col]  == "0"
        def bfs(row, col, grid):
            queue = collections.deque()
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for row, col in directions:
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1":
                        queue.append((row, col))
                        grid[row][col] = "0"

        if not grid:
            return 0

        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    # dfs(row, col, grid)
                    bfs(row, col, grid)
                    islands += 1

        return islands


if __name__ == '__main__':
    so = Solution()
    print(so.numIslands(grid=[["1", "0", "1", "1", "0"],
                              ["0", "1", "0", "1", "0"],
                              ["1", "1", "0", "0", "0"],
                              ["0", "0", "0", "0", "0"]]))
