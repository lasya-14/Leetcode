class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res=[]
        def noZero(x: int) -> bool:
            return '0' not in str(x)
        for i in range(1,n):
            if noZero(i) and noZero(n-i):
                res.append(i)
                res.append(n-i)
                break
        return res


        