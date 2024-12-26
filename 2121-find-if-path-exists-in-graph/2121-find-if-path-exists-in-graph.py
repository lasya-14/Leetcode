class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        p={i:[] for i in range(n)}
        for i,j in edges:
            p[i].append(j)
            p[j].append(i)
        visited=set()
        def dfs(c):
            if c==destination:
                return True
            if c not in visited:
                visited.add(c)
                for i in p[c]:
                    if dfs(i):
                        return True
            return False
        return dfs(source)