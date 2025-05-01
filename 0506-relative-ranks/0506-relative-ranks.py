class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        res=[""]*n
        scored_index=[]
        for i in range(n):
            scored_index.append((score[i],i))
        scored_index.sort(reverse=True)
        for char in range(n):
            val,index=scored_index[char]
            if char==0:
                res[index]="Gold Medal"
            elif char==1:
                res[index]="Silver Medal"
            elif char==2:
                res[index]="Bronze Medal"
            else:
                res[index]=str(char+1)
        return res
        

        