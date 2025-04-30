class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapping={')':'(','}':'{',']':'['}
        for i in s:
            if i in mapping.values():
                st.append(i)
            else:
                if not st or st[-1]!=mapping[i]:
                    return False
                st.pop()
        if not st:
            return True
        else:
            return False
