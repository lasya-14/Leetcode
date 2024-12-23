class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mx=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                    length=len(words[i])*len(words[j])
                    p=set(words[i]) & set(words[j])
                    if len(p)==0:
                        if length>mx:
                            mx=length
        return mx

        