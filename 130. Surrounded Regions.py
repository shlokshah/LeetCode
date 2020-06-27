'''Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.'''

class Solution:
    def dfs(self, board, i, j):
        if i>len(board)-1 or i<0 or j>len(board[0])-1 or j<0:
            return
        if board[i][j]=="O":
            board[i][j]="*"
        if i>1 and board[i-1][j]=="O":
            self.dfs(board, i-1, j)
        if i<len(board)-2 and board[i+1][j]=="O":
            self.dfs(board, i+1, j)
        if j>1 and board[i][j-1]=="O":
            self.dfs(board, i, j-1)
        if j<len(board[0])-2 and board[i][j+1]=="0":
            self.dfs(board, i, j+1)

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board): return
        rows=len(board)
        columns = len(board[0])

        for j in range(columns):
            if board[0][j] == "O":
                self.dfs(board, 0, j)
            if board[rows-1][j]=="O":
                self.dfs(board, rows-1, j)

        for i in range(rows):
            if board[i][0]=="O":
                self.dfs(board, i, 0)
            if board[i][columns-1]=="O":
                self.dfs(board, i, columns-1)

        for i in range(rows):
            for j in range(columns):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="*":
                    board[i][j]="O"


A=Solution()
A.solve([["X", "O", "X"], ["O", "X","O"],["X", "O", "X"]])
#["X", "X", "X", "X"],["X", "O", "O", "X"],["X", "X", "O", "X"],["X", "O", "X", "X"]