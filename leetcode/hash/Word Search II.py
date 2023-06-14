from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(row, col, trie_root):
            char = board[row][col]
            cur = trie_root[char]
            word = cur.pop("Found", False)
            if word:
                result.append(word)
            board[row][col] = "seen"
            directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for r, c in directions:
                if 0 <= r < rows and 0 <= c < cols and board[r][c] in cur:
                    dfs(r, c, cur)
            board[row][col] = char

        trie = {}
        for word in words:
            cur = trie
            for char in word:
                cur = cur.setdefault(char, {})
            cur["Found"] = word

        rows = len(board)
        cols = len(board[0])
        result = []
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return result


if __name__ == '__main__':
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    so = Solution()
    print(so.findWords(board, words))
