class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        pairs=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                pairs.append((words[i],words[j]))
        c=0
        for i,j in pairs:
            n=len(i)
            if i in j[:n] and i in j[-n:]:
                c+=1
        return c
        