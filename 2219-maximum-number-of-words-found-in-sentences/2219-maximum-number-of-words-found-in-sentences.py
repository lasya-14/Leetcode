class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for i in sentences:
            spaces=i.count(' ')
            if spaces>count:
                count=spaces
        return count+1
        