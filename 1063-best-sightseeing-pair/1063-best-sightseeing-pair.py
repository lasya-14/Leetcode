class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        m=float('-inf')
        mx=values[0]
        for i in range(1,len(values)):
            m=max(m,mx+values[i]-i)
            mx=max(mx,values[i]+i)
        return m