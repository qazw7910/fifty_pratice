def main():
    so = Solution()
    print(so.shiftGrid(grid=[[1,1],[2,3],[3,5],[4,3],[7,2],[6,1],[5,1]], k=23))


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        col = len(grid[0])
        row = len(grid)

        def separateGrid(grid):
            space = []
            for i in grid:
                for j in i:
                    space.append(j)
            return space

        def combineGrid(grid, row, col):
            space = [[0 for i in range(col)] for j in range(row)]
            for i in range(row):
                for j in range(col):
                    space[i][j] = grid[i * col + j]
            return space

        grid = separateGrid(grid)
        k = k % (row * col)
        grid[:] = grid[-k:] + grid[:-k]
        grid = combineGrid(grid, row, col)
        return grid
if __name__ == '__main__':
    main()
