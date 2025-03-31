class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1=s+s
        s2=s1[1:-1]
        if s in s2:
            return True
        else:
            return False