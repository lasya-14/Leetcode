class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d=collections.Counter(s)
        p=set()
        st=[]
        for i in s:
            if i not in p:
                while st and st[-1]>i and d[st[-1]]>0:
                    p.discard(st.pop())
                st.append(i)
                p.add(i)
            d[i]-=1
        return ''.join(st)
