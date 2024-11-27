class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        n=len(s)//2
        m=len(s)
        for i in range(n):
            l=s[i]
            r=s[m-1-i]
            if l!=r:
                return False
        else:
            return True