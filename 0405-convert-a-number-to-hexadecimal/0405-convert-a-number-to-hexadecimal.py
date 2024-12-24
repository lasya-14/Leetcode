class Solution:
    def toHex(self, num: int) -> str:
        d={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        op=''
        if num<0:
            num+=2**32
        if num==0:
            return "0"
        while num>0:
            r=num%16
            if r in d:
                op+=d[r]
            else:
                op+=str(r)
            num//=16
        return op[::-1]
        