class Solution:
    def simplifyPath(self, path: str) -> str:
        s=path.split('/')
        st=[]
        for i in s:
            if st and i=='..':
                st.pop()
            elif i in ['.','','/','..']:
                continue
            else:
                st.append(i)
        r='/'+'/'.join(st)
        return r
        