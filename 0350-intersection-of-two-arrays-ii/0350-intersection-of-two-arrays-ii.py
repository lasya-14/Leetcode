class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=collections.Counter(nums1)
        e=collections.Counter(nums2)
        p=[]
        for i in d:
            if i in e:
                p.extend([i]*min(d[i],e[i]))
        return p