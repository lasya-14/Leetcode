class Solution:
    def integerReplacement(self, n: int) -> int:
        count=0
        while n!=1:
            if n==3:
                count+=2
                return count
            if (n&1)==0:
                n//=2
            elif ((n//2)&1)==1:
                    n+=1
            else:
                n-=1
            count+=1
        return count


        