class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p=[]
        for i in nums1:
            if i in nums2:
                p.append(i)
                nums2.remove(i)
            else:
                continue
        return p
        