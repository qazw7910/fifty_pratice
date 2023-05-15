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
                for x, y in directions:
                    if not x < 0 and not x == len(grid) and not y < 0 and not y == len(grid[0]) and not grid[x][y] == "0":
                        # if 1 in four directions append (x, y) to queue to keep recursion
                        queue.append((x, y))
                        grid[x][y] = "0"

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
