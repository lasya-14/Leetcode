class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p=[]
        for i in matrix:
            p+=i
        p.sort()
        l,h=0,len(p)-1
        while l<=h:
            mid=(l+h)//2
            if target>p[mid]:
                l=mid+1
            elif target<p[mid]:
                h=mid-1
            else:
                return True
        return False
        