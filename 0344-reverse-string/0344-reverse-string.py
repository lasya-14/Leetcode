class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st=list(s)
        for i in range(len(st)):
            s[i]=st.pop()