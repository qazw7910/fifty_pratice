import collections
from typing import List


class Solution:
    # if arrived
    def numIslands(self, grid: List[List[str]]) -> int:
        def find_islands(row, col, grid):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != "1":
                return

            grid[row][col] = "0"

            directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for r, c in directions:
                find_islands(r, c, grid)

        # original grid[row][col] == "1" but near  grid[row][col]  == "0"
        def bfs(row, col, grid):
            queue = collections.deque()
            queue.append((row, col))

            while queue:
                r, c = queue.popleft()
                directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for r, c in directions:
                    if not r < 0 and not r == len(grid) and not c < 0 and not c == len(grid[0]) and grid[r][c] == "1":
                        # if 1 in four directions append (x, y) to queue to keep recursion
                        queue.append((r, c))
                        grid[r][c] = "0"

        if not grid:
            return 0

        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    # find_islands(row, col, grid)
                    bfs(row, col, grid)
                    islands += 1

        return islands


if __name__ == '__main__':
    so = Solution()
    print(so.numIslands(grid=[["1", "0", "1", "1", "0"],
                              ["0", "1", "0", "1", "0"],
                              ["1", "1", "0", "0", "0"],
                              ["0", "0", "0", "0", "0"]]))
