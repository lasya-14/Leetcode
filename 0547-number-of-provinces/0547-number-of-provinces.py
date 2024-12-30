class UnionFind:
    def __init__(self,n):
        self.x=list(range(n))
    def union(self,a,b):
        ra,rb=self.find(a),self.find(b)
        if ra!=rb:
            self.x[ra]=rb
        return a
    def find(self,a):
        while self.x[a]!=a:
            a=self.x[a]
        return a
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        s=len(isConnected)
        obj=UnionFind(s)
        for i in range(s):
            for j in range(i,s):
                if isConnected[i][j]==1:
                    obj.union(i,j)
        return len(set([obj.find(i) for i in range(s)]))
        