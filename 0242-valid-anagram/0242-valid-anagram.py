class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=Counter(s)
        f=Counter(t)
        return True if d==f else False