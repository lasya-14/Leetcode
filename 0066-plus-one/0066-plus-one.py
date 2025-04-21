class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=''
        for i in range(len(digits)):
            res+=str(digits[i])
        ans=int(res)+1
        return [int(d) for d in str(ans)]
        