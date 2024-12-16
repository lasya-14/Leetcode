class Solution:
    def checkValidString(self, s: str) -> bool:
        st=[]
        star=[]
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            elif s[i]==')':
                if st:
                    st.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        while len(st)>0 and len(star)>0:
            if st[-1]>star[-1]:
                return False
            star.pop()
            st.pop()
        return len(st)==0


       