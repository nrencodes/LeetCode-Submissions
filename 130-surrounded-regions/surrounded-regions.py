class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])\

        def dfs(r, c):
            if(r < 0 or c < 0 or r == m or c == n
                or board[r][c] != "O"):
                return

            board[r][c] = "T"
            for nr, nc in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(r + nr, c + nc)

        for row in range(m):
            for col in range(n):
                if (board[row][col] == "O"
                   and (row in [0, m - 1] or col in [0, n - 1])):
                   dfs(row, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(m):
            for col in range(n):
                if board[row][col] == "T":
                    board[row][col] = "O"
