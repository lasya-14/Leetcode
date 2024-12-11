class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff=(sum(aliceSizes)-sum(bobSizes))//2
        a=set(aliceSizes)
        for c in set(bobSizes):
            if c+diff in a:
                return [c+diff,c]
        