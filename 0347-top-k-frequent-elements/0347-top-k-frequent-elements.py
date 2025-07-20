class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        res=[]
        s=sorted(d.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(s[i][0])
        return res
        