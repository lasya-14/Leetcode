class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stri=''.join(c.lower() for c in s if c.isalnum())
        n=len(stri)//2
        for i in range(n):
            if stri[i]!=stri[len(stri)-1-i]:
                return False
        return True