class Solution:
    def trap(self, height: List[int]) -> int:
        i,j,lmax,rmax,tot=0,len(height)-1,0,0,0
        while i<=j:
            lmax=max(lmax,height[i])
            rmax=max(rmax,height[j])
            if lmax<=rmax:
                tot+=lmax-height[i]
                i+=1
            else:
                tot+=rmax-height[j]
                j-=1
        return tot 
        