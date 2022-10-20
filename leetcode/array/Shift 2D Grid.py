def main():
    so = Solution()
    print(so.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        row = len(grid)
        col = len(grid[0])

        def separate(grid):
            space = []
            for i in grid:
                for j in i:
                    space.append(j)
            return space

        def combine(grid, row, col):
            space = [[0 for i in range(col)]for j in range(row)]
            for i in range(row):
                for j in range(col):
                    space[i][j] = grid[i * col + j]
            return space

        grid = separate(grid)
        k = k % (col * row)
        grid[:] = grid[-k:] + grid[:-k]
        grid = combine(grid, row, col)
        return grid


if __name__ == '__main__':
    main()
