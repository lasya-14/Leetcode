class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row,col = len(maze),len(maze[0])
        q = deque()
        q.append([entrance[0],entrance[1],-1])
        while q:
            r,c,dist = q.popleft()
            if not (0<=r<row and 0<=c<col): #check if it reached the end of the grid
                if dist>0:
                    return dist
                continue
            if maze[r][c] == '+':
                continue
            maze[r][c] = '+' #make the cell blocked as it is visited
            for newr,newc in [(0,1),(0,-1),(1,0),(-1,0)]:
                q.append([r+newr,c+newc,dist+1])
        return -1