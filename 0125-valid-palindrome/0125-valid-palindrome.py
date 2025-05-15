class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=''
        for i in s.lower():
            if i.isalnum():
                s2+=i
        i=0
        j=len(s2)-1
        is_palindrome=False
        while i<j:
            if s2[i]==s2[j]:
                is_palindrome=True
            else:
                return False
            i+=1
            j-=1
        return True
