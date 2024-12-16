class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def getMaximum(rows):
            mx=0
            st=[]
            for i,j in enumerate(rows):
                start=i
                while st and st[-1][-1]>j:
                    w,h=st.pop()
                    start=w
                    mx=max(mx,h*(i-w))
                st.append((start,j))
            for i,j in st:
                mx=max(mx,j*(len(rows)-i))
            return mx
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=int(matrix[i][j])
        t=[0]*len(matrix[0])
        mx=0
        area=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    t[j]=0
                else:
                    t[j]+=matrix[i][j]
            area=getMaximum(t)
            if area>mx:
                mx=area
        return mx
        