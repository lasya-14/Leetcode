class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res=0
        for operation in operations:
            if operation in ("X++","++X"):
                res+=1
            elif operation in ("X--","--X"):
                res-=1
        return res


        