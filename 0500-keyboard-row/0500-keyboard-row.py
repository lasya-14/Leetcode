class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        frow="qwertyuiop"
        mrow="asdfghjkl"
        lrow="zxcvbnm"
        res=[]
        for word in words:
            b_row1=all(letter in frow for letter in word.lower())
            b_row2=all(letter in mrow for letter in word.lower())
            b_row3=all(letter in lrow for letter in word.lower())
            if b_row1 or b_row2 or b_row3:
                res.append(word)
        
        return res
        