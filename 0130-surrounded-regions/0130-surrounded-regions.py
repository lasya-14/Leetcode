class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            board[r][c] = 'T'
            for dr,dc in (-1,0),(0,-1),(0,1),(1,0):
                new_row,new_col = dr+r, dc+c
                if new_col<0 or new_row<0 or new_row>=rows or new_col>=cols or board[new_row][new_col]!='O':
                    continue
                dfs(new_row,new_col)

        for i in [0,rows-1]:
            for j in range(cols):
                if board[i][j] == 'O':
                    dfs(i,j)
        for j in [0,cols-1]:
            for i in range(1,rows-1):
                if board[i][j] == 'O':
                    dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'