class Solution:
    def stringSequence(self, t: str) -> List[str]:
        return [t[:i] + chr(a) for i, ch in enumerate(t) for a in range(ord("a"), ord(ch) + 1)]