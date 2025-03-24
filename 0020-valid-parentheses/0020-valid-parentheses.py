class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        mapping={')':'(',']':'[','}':'{'}
        for char in s:
            if char in mapping.values():
                st.append(char)
            else:
                if not st or st[-1]!=mapping[char]:
                    return False
                st.pop()
        return not st

        