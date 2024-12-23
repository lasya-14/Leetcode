class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)
        count=0
        s=str(b)
        for i in s:
            if i=='1':
                count+=1
            else:
                continue
        return count

        