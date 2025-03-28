class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=Counter(s)
        d1=Counter(t)
        return True if d==d1 else False