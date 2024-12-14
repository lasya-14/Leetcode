class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        res=0
        st=[]
        for i in heights:
            start=0
            while st and st[-1][-1]>i:
                w,h=st.pop()
                start+=w
                res=max(res,start*h)
            st.append((start+1,i))
        return res

        