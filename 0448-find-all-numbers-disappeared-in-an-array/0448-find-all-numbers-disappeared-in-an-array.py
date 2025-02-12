class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        s=[]
        d=Counter(nums)
        for i in range(1,len(nums)+1):
            l.append(i)
        for i in l:
            if i not in d.keys():
                s.append(i)
        return s
        