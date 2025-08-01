class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        resp=[[1]]
        for i in range(numRows-1):
            res=[0]+resp[-1]+[0]
            row=[]
            for j in range(len(resp[-1])+1):
                row.append(res[j]+res[j+1])
            resp.append(row)
        return resp
        
        