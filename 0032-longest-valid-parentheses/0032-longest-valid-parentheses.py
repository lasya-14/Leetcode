class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        tot=0
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            elif s[i]==')':
                st.pop()
                if not st:
                    st.append(i)
                else:
                    tot=max(tot,i-st[-1])
        return tot
