class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev=0
        x1=x
        while x1>0:
            rem=x1%10
            rev=rev*10+rem
            x1=x1//10

        if rev==x:
            return True
        return False