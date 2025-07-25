class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW,COL=len(board),len(board[0])
        visited=set()
        def dfs(board,word,r,c,i):
            if i==len(word):
                return True
            if r<0 or r==ROW or c<0 or c==COL or (r,c) in visited or board[r][c]!=word[i]:
                return
            visited.add((r,c))
            res=(dfs(board,word,r-1,c,i+1) or
            dfs(board,word,r,c-1,i+1) or
            dfs(board,word,r+1,c,i+1) or
            dfs(board,word,r,c+1,i+1))
            visited.remove((r,c))
            return res
        for r in range(ROW):
            for c in range(COL):
                if dfs(board,word,r,c,0):
                    return True
        return False