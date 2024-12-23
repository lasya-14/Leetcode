class Solution:
    def countBits(self, n: int) -> List[int]:
        li=[]
        for i in range(n+1):
            b=bin(i)
            s=str(b)
            li.append(s.count('1'))
        return li