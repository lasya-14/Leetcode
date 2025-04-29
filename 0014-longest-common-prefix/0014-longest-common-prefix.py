class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=strs[0]
        for i in strs[1:]:
            while not i.startswith(res):
                res=res[:-1]
                if not res:
                    return ""
        return res
            