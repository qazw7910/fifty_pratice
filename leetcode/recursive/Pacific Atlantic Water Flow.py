from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_visited = set()
        atlantic_visited = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, visited, prev_heights):
            if ((r, c) in visited or r < 0 or r == rows or c < 0 or c == cols or heights[r][c] < prev_heights):
                return

            visited.add((r, c))
            # top,down,right,left
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        # pacific and atlantic row
        for i in range(cols):
            # pacific ocean row
            dfs(0, i, pacific_visited, heights[0][i])
            # atlnatic ocean row
            dfs(rows - 1, i, atlantic_visited, heights[rows - 1][i])

        # pacific and atlantic col
        for row in range(rows):
            # pacific ocean col
            dfs(row, 0, pacific_visited, heights[row][0])
            # atlnatic ocean col
            dfs(row, cols - 1, atlantic_visited, heights[row][cols - 1])

        # return method 1
        results = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_visited and (row, col) in atlantic_visited:
                    results.append([row, col])

        return results
        # return method 2
        # return list(pacific_visited.intersection(atlantic_visited))


if __name__ == '__main__':
    so = Solution()
    print(so.pacificAtlantic(
        heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
