class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        char=s.split()
        return len(char[-1])
        

        
        