class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        cols,pos,neg,res=set(),set(),set(),[]
        board=[['.']*n for i in range(n)]
        def backtrack(r):
            if r==n:
                res.append([''.join(p) for p in board])
                return
            for c in range(n):
                if c in cols or r+c in pos or r-c in neg or board[r][c]=='Q':
                    continue
                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c]='Q'
                backtrack(r+1)
                board[r][c]='.'
                cols.discard(c)
                pos.discard(r+c)
                neg.discard(r-c)
        backtrack(0)
        return len(res)