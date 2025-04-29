class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        ans=''
        d1=dict(sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True))
        
        for i,j in d1.items():
            ans+=i*j
        return ans

        