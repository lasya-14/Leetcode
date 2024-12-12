class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        diff=0
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    diffv=abs(i-j)
                    diff=max(diff,diffv)
        return diff

        